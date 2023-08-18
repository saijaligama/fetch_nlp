from flask import Blueprint, render_template, request, redirect, url_for, session, flash, send_file, make_response, \
    Response, jsonify
import random
from mongo_utility import  MongoDBManager

bp = Blueprint('view', __name__, url_prefix='/uncg_math', template_folder="./templates", static_folder="./static")

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

if __name__ == '__main__':
   app.run(port=8005,debug=True)