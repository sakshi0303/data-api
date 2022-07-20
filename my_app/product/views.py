from werkzeug.exceptions import abort
from flask import render_template
from flask import Blueprint, request
import json

from my_app.product.models import PRODUCTS
from my_app.product.ddbclient import DDBClient

product_blueprint = Blueprint('product', __name__)

ddbData = {}
ddbClient = DDBClient()

@product_blueprint.route('/')
@product_blueprint.route('/home')
def home():
    return render_template('home.html', products=PRODUCTS)

# A button that opens the upload page
# On the upload page user drops the file
# upload API to save the file in DDB
@product_blueprint.route('/upload', methods = ['POST', 'GET'])
def upload():
    # # 1. Transform post request to json and extract content
    uploaded_file = request.files['file']
    jsonData = json.loads(uploaded_file.read())
    # jsonData = json.loads(request.data)
    print('namespace: ', jsonData["namespace"])
    print('content: ', jsonData["content"])
    print('fileName: ', jsonData["fileName"])

    # 2. Check if table exists and create if not
    ddbClient.createTable(jsonData["namespace"], jsonData["content"])

    # 3. Upload the data to DDB table
    ddbClient.upload(jsonData["namespace"], jsonData["content"])

    return render_template('upload.html', products=PRODUCTS)

@product_blueprint.route('/product/<key>')
def product(key):
    product = PRODUCTS.get(key)
    if not product:
        abort(404)
    return render_template('product.html', product=product)
