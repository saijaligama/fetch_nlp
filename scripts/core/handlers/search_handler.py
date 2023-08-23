import pandas as pd
import numpy as np
from fuzzywuzzy import process
from scripts.utils.data_loader import DataLoader
from scripts.utils.category_util import category_offer


class SearchHandler:
    SIMILARITY_THRESHOLD = 80

    def __init__(self):
        data_loader = DataLoader()
        self.brand_df, self.category_df, self.offers_df = data_loader.get_dfs()

        self.merged_df = self._merge_dfs()

        self.category_vocab_1 = self.category_df['PRODUCT_CATEGORY'].unique()
        self.category_vocab_2 = self.category_df['IS_CHILD_CATEGORY_TO'].unique()

    def _merge_dfs(self):
        merged_df = pd.merge(self.brand_df, self.category_df, left_on="BRAND_BELONGS_TO_CATEGORY"
                             , right_on="PRODUCT_CATEGORY")
        merged_df = pd.merge(merged_df, self.offers_df, on='BRAND')
        return merged_df

    def search(self, query):

        categories = self._fuzzy_search_categories(query)
        brands = self._fuzzy_search_brands(query)
        retailers = self._fuzzy_search_retailers(query)

        if categories.score > brands.score and categories.score > retailers.score:
            results = self._get_category_results(categories.match)
            formatted_results = self._format_results(categories.match, categories.score, query)
            results.update(formatted_results)
            return results

        elif brands.score > categories.score and brands.score > retailers.score:
            results = self._get_brand_results(brands.match)
            # print(type(results))
            formatted_results = self._format_results(brands.match, brands.score, query)
            results.update(formatted_results)
            return results

        else:
            results = self._get_retailer_results(retailers.match)
            formatted_results = self._format_results(retailers.match, retailers.score, query)
            results.update(formatted_results)
            return results

    def _fuzzy_search_categories(self, query):
        choices = np.concatenate((self.category_vocab_1, self.category_vocab_2))
        match, score = process.extractOne(query, choices)
        return FuzzySearchResult(match, score)

    def _fuzzy_search_brands(self, query):
        choices = self.brand_df['BRAND'].unique()
        match, score = process.extractOne(query, choices)
        return FuzzySearchResult(match, score)

    def _fuzzy_search_retailers(self, query):
        choices = self.offers_df['RETAILER'].unique()
        match, score = process.extractOne(query, choices)
        return FuzzySearchResult(match, score)

    def _get_category_results(self, category):
        category_df = category_offer(self.category_vocab_2, self.category_vocab_1, self.category_df,
                                     self.brand_df, self.offers_df, category)
        result = {'results': category_df['OFFER'].tolist()}
        return result

    def _get_brand_results(self, brand):
        brand_df = self.merged_df[self.merged_df['BRAND'] == brand]
        result = {'results': brand_df['OFFER'].tolist()}
        return result

    def _get_retailer_results(self, retailer):
        retailer_df = self.merged_df[self.merged_df['RETAILER'] == retailer]
        result = {'results': retailer_df['OFFER'].tolist()}
        return result

    def _format_results(self, match, score, query):
        results = {}

        if score >= self.SIMILARITY_THRESHOLD:
            results['Original Word'] = f"Original word: {query}"
        else:
            results['Original Word'] = f"No suitable correction found for '{query}'"

        results['Best Match'] = f"Best match: {match}"
        results['Similarity Score'] = f"Similarity score: {score}"

        return results


class FuzzySearchResult:
    def __init__(self, match, score):
        self.match = match
        self.score = score
