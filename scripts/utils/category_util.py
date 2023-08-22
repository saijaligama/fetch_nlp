# category_utils.py

import pandas as pd


# def category_offer(category_vocab_2, category_vocab_1, categories_df, brands_df, offers_df, best_match):

def category_offer(category_vocab_2, category_vocab_1, categories, brandCategory, offerRetailer, best_match):
    # similarity(similarityScore, similarity_threshold, best_match, input_word)
    brand_cat = []

    if best_match in category_vocab_2:
        child_category = list(categories[categories.IS_CHILD_CATEGORY_TO == best_match]['PRODUCT_CATEGORY'])
        brand_cat = []
        for cc in child_category:
            brand_cat.extend(list(brandCategory[brandCategory.BRAND_BELONGS_TO_CATEGORY == cc]['BRAND']))
    elif best_match in category_vocab_1:
        child_category = list(categories[categories.PRODUCT_CATEGORY == best_match]['PRODUCT_CATEGORY'])
        brand_cat = []
        for cc in child_category:
            brand_cat.extend(list(brandCategory[brandCategory.BRAND_BELONGS_TO_CATEGORY == cc]['BRAND']))
    else:
        return ["No offer currently"]
    offer_brand = offerRetailer.BRAND.unique()

    df = pd.DataFrame()
    # for bc in set(brand_cat): if bc in offer_brand: df = pd.concat([df,offerRetailer[offerRetailer.BRAND==bc][[
    # 'OFFER','BRAND','RETAILER']]],axis=0, ignore_index=True) print(df)
    for bc in set(brand_cat):
        if bc in offer_brand:
            df = pd.concat([df, offerRetailer[offerRetailer.BRAND == bc]], axis=0, ignore_index=True)
            # return offerRetailer[offerRetailer.BRAND == bc][['OFFER']].reset_index(
            #     drop=True).to_list()
            # return offerRetailer[offerRetailer.BRAND == bc]['OFFER'].reset_index(
            #     drop=True).to_list()
            # print(offerRetailer[offerRetailer.BRAND == bc]['OFFER'])
    if not df.empty:
        return df
    else:
        return df
