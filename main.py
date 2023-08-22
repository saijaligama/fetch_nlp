from flask import Flask
from scripts.services import search_service
from scripts.services import home_service

app = Flask(__name__)

# Register routes
app.register_blueprint(home_service.home)
app.register_blueprint(search_service.search_service_bp)


if __name__ == '__main__':
    app.run(port=8005, debug=True)




# from flask import Blueprint, render_template, request, redirect, url_for, session, flash, send_file, make_response, \
#     Response, jsonify, Flask
# import pandas as pd
# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process
# import random
#
# # from mongo_utility import  MongoDBManager
#
# bp = Blueprint('view', __name__, url_prefix='/fetch_rewards', template_folder="./templates", static_folder="./static")
#
# # from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/', methods=["GET", "POST"])
# def home():
#     return render_template('home_page.html')
#
#
# def similarity(similarity_score, similarity_threshold, best_match, input_word):
#     search_results = {}
#     if similarity_score >= similarity_threshold:
#         search_results['Original Word'] = f"Original word: {input_word}"
#     else:
#         search_results['Original Word'] = f"No suitable correction found for '{input_word}'."
#
#     search_results['Best Match'] = f"Best match: {best_match}"
#     search_results['Similarity Score'] = f"Similarity score: {similarity_score}"
#
#     return search_results
#
#
# def get_offer(vocab, vocab_type, similarity_score, similarity_threshold, best_match, input_word, offerRetailer):
#     # search_results = {}
#     # search_results = similarity(similarity_score, similarity_threshold, best_match, input_word)
#
#     if best_match in vocab:
#         return offerRetailer[offerRetailer[vocab_type] == best_match]['OFFER'].reset_index(
#             drop=True).to_list()
#         # print(offerRetailer[offerRetailer.RETAILER==bestMatch]['OFFER'].reset_index(drop=True).to_list())
#     else:
#         return [f"Currently there are no offers for {best_match}"]
#
#     # return search_results
#     # print(f"Currently there are no offers for {bestMatch}")
#
#
# def category_offer(category_vocab_2, category_vocab_1, categories, brandCategory, offerRetailer, best_match):
#     # similarity(similarityScore, similarity_threshold, best_match, input_word)
#     brand_cat = []
#
#     if best_match in category_vocab_2:
#         child_category = list(categories[categories.IS_CHILD_CATEGORY_TO == best_match]['PRODUCT_CATEGORY'])
#         brand_cat = []
#         for cc in child_category:
#             brand_cat.extend(list(brandCategory[brandCategory.BRAND_BELONGS_TO_CATEGORY == cc]['BRAND']))
#     elif best_match in category_vocab_1:
#         child_category = list(categories[categories.PRODUCT_CATEGORY == best_match]['PRODUCT_CATEGORY'])
#         brand_cat = []
#         for cc in child_category:
#             brand_cat.extend(list(brandCategory[brandCategory.BRAND_BELONGS_TO_CATEGORY == cc]['BRAND']))
#     else:
#         return ["No offer currently"]
#     offer_brand = offerRetailer.BRAND.unique()
#
#     df = pd.DataFrame()
#     # for bc in set(brand_cat): if bc in offer_brand: df = pd.concat([df,offerRetailer[offerRetailer.BRAND==bc][[
#     # 'OFFER','BRAND','RETAILER']]],axis=0, ignore_index=True) print(df)
#     for bc in set(brand_cat):
#         if bc in offer_brand:
#             df = pd.concat([df,offerRetailer[offerRetailer.BRAND == bc]],axis=0, ignore_index=True)
#             # return offerRetailer[offerRetailer.BRAND == bc][['OFFER']].reset_index(
#             #     drop=True).to_list()
#             # return offerRetailer[offerRetailer.BRAND == bc]['OFFER'].reset_index(
#             #     drop=True).to_list()
#             # print(offerRetailer[offerRetailer.BRAND == bc]['OFFER'])
#     if not df.empty:
#         return df['OFFER'].to_list()
#     else:
#         return ["No offer currently"]
#
#
# @app.route('/search', methods=["GET", "POST"])
# def search():
#     if request.method == "POST":
#         data = request.json
#         input_word = data['search_item']
#         brandCategory = pd.read_csv("static/data/brand_category.csv")
#         categories = pd.read_csv("static/data/categories.csv")
#         offerRetailer = pd.read_csv("static/data/offer_retailer.csv")
#
#         catBrandCat = pd.merge(brandCategory, categories, left_on="BRAND_BELONGS_TO_CATEGORY",
#                                right_on="PRODUCT_CATEGORY")
#
#         ###print(categories.shape,brandCategory.shape, catBrandCat.shape)
#
#         catBrandRetailer = pd.merge(catBrandCat, offerRetailer, on="BRAND")
#
#         # print(catBrandRetailer.shape, len(catBrandRetailer.RETAILER.unique()))
#
#         retailerVocab = catBrandRetailer.RETAILER.unique()
#         retailerVocabAll = offerRetailer.RETAILER.unique()
#
#         brand_vocab = catBrandRetailer.BRAND.unique()
#         brand_vocab_all = brandCategory.BRAND.unique()
#
#         category_vocab_1 = list(categories.PRODUCT_CATEGORY.unique())
#         category_vocab_2 = categories.IS_CHILD_CATEGORY_TO.unique()
#         category_vocab_1.extend(category_vocab_2)
#
#         best_match_cc, similarity_score_cc = process.extractOne(input_word, category_vocab_1)
#         best_match_brand, similarity_score_brand = process.extractOne(input_word, brand_vocab_all)
#         best_match_retail, similarity_score_retail = process.extractOne(input_word, retailerVocabAll)
#
#         # similarity_score = 0
#         similarity_threshold = 30
#
#         print('similarity_score_cc ', similarity_score_cc)
#         print('similarity_score_brand ', similarity_score_brand)
#         print('similarity_score_retail ', similarity_score_retail)
#
#         search_results = {}
#
#         if similarity_score_cc >= similarity_score_brand and similarity_score_cc > similarity_score_retail:
#             search_results = similarity(similarity_score_cc, similarity_threshold, best_match_cc, input_word)
#             search_results['results'] = category_offer(category_vocab_2, category_vocab_1, categories, brandCategory,
#                                                        offerRetailer, best_match_cc)
#
#         elif similarity_score_brand > similarity_score_cc and similarity_score_brand >= similarity_score_retail:
#             search_results = similarity(similarity_score_brand, similarity_threshold, best_match_brand, input_word)
#             search_results['results'] = get_offer(brand_vocab_all, 'BRAND', similarity_score_brand, similarity_threshold,
#                                                   best_match_brand, input_word, offerRetailer)
#
#         elif similarity_score_retail > similarity_score_brand and similarity_score_retail > similarity_score_cc:
#             search_results = similarity(similarity_score_retail, similarity_threshold, best_match_retail, input_word)
#             search_results['results'] = get_offer(retailerVocabAll, 'RETAILER', similarity_score_retail, similarity_threshold,
#                                                   best_match_retail, input_word, offerRetailer)
#
#         return jsonify(search_results)
#
#
# if __name__ == '__main__':
#     app.run(port=8005, debug=True)
