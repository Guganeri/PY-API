from flask import Flask, jsonify, Response
from dotenv import load_dotenv
from bson.json_util import dumps
import json
import pymongo
import os
import logging

load_dotenv()
BDURL = os.getenv("BDURL")

client = pymongo.MongoClient(BDURL)
db = client.api_cat
catCollection = db['api_cat']
hatCatCollection = db['hat_Cat']
glassCatCollection = db['glass_Cat']
 
### Logs inf ###
logging.basicConfig(filename='meow.log', level=logging.DEBUG)


### API ROUTES INICIO ###
app = Flask("API-CAT")

### API_CAT ###
@app.route('/', methods=['GET'])
def home():    
    return "API-CAT", 200   

### Listar todas as raças ###
@app.route('/listar-racas/', methods=['GET'])
def listar_racas():      
    cats = list(catCollection.find())    
    if (cats == []):
        response = Response(status=404)
        return response
    else:
        response = Response(status=200, headers={}, response=dumps(cats), mimetype='application/json')
        return response

### Listar informações partindo de uma raça ###
@app.route('/listar-racas/<string:raca>/', methods=['GET'])     
def listar_racas_inf(raca):
    cats = list(catCollection.find({"id": raca}))
    if (cats == []):
        response = Response(status=404)
        return response
    else:
        response = Response(status=200, headers={}, response=dumps(cats), mimetype='application/json')
        return response

### Listar raças partindo de um temperamento ###
@app.route('/listar-racas/temperamento/<string:temperamento>/', methods=['GET'])
def listar_racas_temperamento(temperamento):
    cats = list(catCollection.find({"temperament": {"$regex": temperamento}}))
    if (cats == []):
        response = Response(status=404)
        return response
    else:
        response = Response(status=200, headers={}, response=dumps(cats), mimetype='application/json')
        return response

### Listar raças partindo de uma origem ### 
@app.route('/listar-racas/origem/<string:origem>/', methods=['GET'])
def listar_racas_origin(origem):
    cats = list(catCollection.find({"origin": origem}))
    if (cats == []):        
        response = Response(status=404)
        return response
    else:
        response = Response(status=200, headers={}, response=dumps(cats), mimetype='application/json')
        return response

### Listar imagem de gatos com chapéu ###
@app.route('/listar/img/chapeu', methods=['GET'])
def listar_img_chapeu():
    cats = list(hatCatCollection.find())
    if (cats == []):
        response = Response(status=404)
        return response
    else:
        response = Response(status=200, headers={}, response=dumps(cats), mimetype='application/json')
        return response

### Listar imagem de gatos com óculus ###
@app.route('/listar/img/oculus', methods=['GET'])
def listar_img_oculus():
    cats = list(glassCatCollection.find())
    if (cats == []):
        response = Response(status=404)
    else:
        response = Response(status=200, headers={}, response=dumps(cats), mimetype='application/json')
        return response 
  
if __name__ == '__main__':
    app.run(debug=False)