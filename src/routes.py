from flask import Flask, jsonify, Response
from dotenv import load_dotenv
from bson.json_util import dumps
import json
import pymongo
import os

load_dotenv()
BDURL = os.getenv("BDURL")

client = pymongo.MongoClient()
db = client.api_cat
catCollection = db['api_cat']

#listAll = list(catCollection.find())
#print(type(listAll))
#print(listAll)    


app = Flask("API-CAT")


@app.route('/', methods=['GET'])
def home():
    return "API-CAT", 200


@app.route('/listar-racas/', methods=['GET'])
def listar_racas():      
    cats = dumps(catCollection.find())
    response = Response(status=200, headers={}, response=cats, mimetype='application/json')
    return response


@app.route('/listar-racas/raca/<string:raca>/', methods=['GET'])     
def listar_racas_inf(raca):
    cats = dumps(catCollection.find({"id": raca}))
    response = Response(status=200, headers={}, response=cats, mimetype='application/json')
    return response

@app.route('/listar-racas/temperamento/<string:temperamento>/', methods=['GET'])
def listar_racas_temperamento(temperamento):
    cats = dumps(catCollection.find({"temperamen": {"$regex": temperamento}}))
    response = Response(status=200, headers={}, response=cats, mimetype='application/json')
    return response


@app.route('/listar-racas/origem/<string:origem>/', methods=['GET'])
def listar_racas_origin(origem):
    cats = dumps(catCollection.find({"origin": origem}))
    response = Response(status=200, headers={}, response=cats, mimetype='application/json')
    return response

  
if __name__ == '__main__':
    app.run(debug=True)
