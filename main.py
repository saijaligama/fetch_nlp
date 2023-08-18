from flask import Blueprint, render_template, request, redirect, url_for, session, flash, send_file, make_response, \
Response, jsonify
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import random
# from mongo_utility import  MongoDBManager

bp = Blueprint('view', __name__, url_prefix='/fetch_rewards', template_folder="./templates", static_folder="./static")

from flask import Flask
app = Flask(__name__)

@app.route('/',methods=["GET", "POST"])
def home():
    return render_template('home_page.html')

@app.route('/search', methods=["GET", "POST"])
def search():
    if request.method == "POST":
        data = request.json
        inputWord = data['search_item']
        brandCategory = pd.read_csv("static/data/brand_category.csv")
        categories = pd.read_csv("static/data/categories.csv")
        offerRetailer = pd.read_csv("static/data/offer_retailer.csv")

        catBrandCat = pd.merge(brandCategory,categories, left_on="BRAND_BELONGS_TO_CATEGORY",right_on="PRODUCT_CATEGORY")

        ###print(categories.shape,brandCategory.shape, catBrandCat.shape)

        catBrandRetailer = pd.merge(catBrandCat,offerRetailer, on="BRAND")

        #print(catBrandRetailer.shape, len(catBrandRetailer.RETAILER.unique()))

        retailerVocab = catBrandRetailer.RETAILER.unique()

        retailerVocabAll = offerRetailer.RETAILER.unique()

        # inputWord = "ACEEME"

        bestMatch, similarityScore = process.extractOne(inputWord, retailerVocabAll)

        # Set a similarity threshold to determine if the input word is a close match
        similarityThreshold = 80

        search_results = {}

        # Check if the best match meets the similarity threshold
        if similarityScore >= similarityThreshold:
            search_results['Original Word'] = f"Original word: {inputWord}"
            search_results['Best Match'] = f"Best match: {bestMatch}"
            search_results['Similarity Score'] = f"Similarity score: {similarityScore}"
            # print(f"Original word: {inputWord}")
            # print(f"Best match: {bestMatch}")
            # print(f"Similarity score: {similarityScore}")
            # print("Spelling corrected!")
        else:
            search_results['Original Word'] = f"No suitable correction found for '{inputWord}'."
            search_results['Best Match'] = f"Best match: {bestMatch}"
            search_results['Similarity Score'] = f"Similarity score: {similarityScore}"
            # print(f"No suitable correction found for '{inputWord}'.")


        if bestMatch in retailerVocab:
            search_results['results'] = offerRetailer[offerRetailer.RETAILER==bestMatch]['OFFER'].reset_index(drop=True).to_list()
            # print(offerRetailer[offerRetailer.RETAILER==bestMatch]['OFFER'].reset_index(drop=True).to_list())
        else:
            search_results['results'] = [f"Currently there are no offers for {bestMatch}"]
            # print(f"Currently there are no offers for {bestMatch}")
        print(search_results)
        return jsonify(search_results)

if __name__ == '__main__':
   app.run(port=8005,debug=True)


