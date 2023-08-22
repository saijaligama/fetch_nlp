# data_loader.py

import pandas as pd


class DataLoader:

    def __init__(self):
        self.brand_df = pd.read_csv("static/data/brand_category.csv")
        self.category_df = pd.read_csv("static/data/categories.csv")
        self.offers_df = pd.read_csv("static/data/offer_retailer.csv")

    def get_dfs(self):
        return self.brand_df, self.category_df, self.offers_df
