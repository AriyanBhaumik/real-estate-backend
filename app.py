import os

import joblib
import pandas as pd
from bson.json_util import dumps
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))

@app.route('/post-listing', methods=['POST'])
@cross_origin()

def post_listing():
    new_property = request.get_json()
    db = client['real_estate']
    collection = db['properties']
    inserted_doc = collection.insert_one(new_property)
    if inserted_doc.acknowledged:
        return jsonify({"message": "Property successfully added!"}), 200
    else:
        return jsonify({"message": "Failed to add property!"}), 400

@app.route('/properties-by-state' , methods=['GET'])
@cross_origin()
def properties_by_state():
    state = request.args.get('state')
    if not state:
        return jsonify({"error": "State parameter is required"}), 400
    db = client['real_estate']
    collection = db['properties']
    properties = collection.find({"state": state})
    properties_list = list(properties)
    return dumps(properties_list), 200, {'Content-Type': 'application/json'}
    
@app.route('/get-loan-amount', methods=['POST'])
@cross_origin()

def get_loan_amout(): 
    payload = request.get_json()
    Gender = int(payload.get('Gender'))
    Education = int(payload.get('Education'))
    Married = int(payload.get('Married'))
    Dependents = min(int(payload.get('Dependents')) , 4)
    Self_Employed = int(payload.get('Self_Employed'))
    ApplicantIncome = int(payload.get('ApplicantIncome'))
    CoapplicantIncome = int(payload.get('CoapplicantIncome'))
    LoanAmount = float(payload.get('LoanAmount'))
    Loan_Amount_Term = int(payload.get('Loan_Amount_Term'))
    Credit_History = int(payload.get('Credit_History'))
    Property_Area = int(payload.get('Property_Area'))

    data = {
    'Gender': [Gender],
    'Married': [Married],
    'Education': [Education],
    'Dependents': [Dependents],
    'Self_Employed': [Self_Employed],
    'ApplicantIncome': [ApplicantIncome],
    'CoapplicantIncome': [CoapplicantIncome],
    'LoanAmount': [LoanAmount],
    'Loan_Amount_Term': [Loan_Amount_Term],
    'Credit_History': [Credit_History],
    'Property_Area': [Property_Area],
    }

    test_data = pd.DataFrame(data , index=[0])
    model = joblib.load(open('./lib/loan_pred.pkl', 'rb'))
    prediction = model.predict(test_data)

    return jsonify({"loan-status": int(prediction[0])}) , 200

@app.route("/house-price-prediction" , methods=['POST'])
@cross_origin()

def house_price_prediction():
    payload = request.get_json()
    HouseSize = float(payload.get('HouseSize' , 0.20))
    PropertySize = float(payload.get('PropertySize' , 0.50))
    Bedrooms = int(payload.get('Bedrooms' , 3 ))
    Bathrooms = int(payload.get('Bathrooms' , 2))

    test_data = pd.DataFrame({
        'bed' : [Bedrooms],
        'bath' : [Bathrooms],
        'acre_lot' : [PropertySize],
        'house_size' : [HouseSize]
    } , index=[0])

    model = joblib.load(open('./lib/house_prices_pred_1.pkl' , 'rb'))
    predictions = model.predict(test_data)

    return jsonify({"house-price" : float(predictions[0])}) , 200


@app.route('/')
def home():
    return "Welcome to the Real Estate Backend!"

if __name__ == '__main__':
    app.run(debug=True)