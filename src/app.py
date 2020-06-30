from flask import Flask, jsonify, Response, request
from flask_web_log import Log
from dotenv import load_dotenv
from bson.json_util import dumps
import json
import pymongo
import os
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import time
import consummer


load_dotenv()


BDURL = os.getenv("BDURL")

client = pymongo.MongoClient(BDURL)
db = client.api_cat
catCollection = db['api_cat']
hatCatCollection = db['hat_Cat']
glassCatCollection = db['glass_Cat']


app = Flask("API-CAT")
app.config["LOG_LOCATION"] = "./logs"
app.config["LOG_TYPE"] = "JSON"
Log(app)


_INF = float('inf')

### Prom ###
graphs = {}
graphs['c'] = Counter('python_request_operations_total',
                      'The total number of processed requests')
graphs['h'] = Histogram('python_request_duration_seconds',
                        'Histogram for the duration in seconds', buckets=(1, 2, 5, 6, 10, _INF))


### API_CAT ###
@app.route('/', methods=['GET'])
def home():
    start = time.time()
    graphs['c'].inc()

    return "API-CAT", 200

    end = time.time()
    graphs['h'].observe(end - start)

### Listar todas as raças ###


@app.route('/listar-racas/', methods=['GET'])
def listar_racas():
    start = time.time()
    graphs['c'].inc()

    cats = list(catCollection.find())
    if (cats == []):
        response = Response(status=404)
        return response
    else:
        response = Response(status=200, headers={}, response=dumps(
            cats), mimetype='application/json')
        return response
    end = time.time()
    graphs['h'].observe(end - start)

### Listar informações partindo de uma raça ###


@app.route('/listar-racas/<string:raca>/', methods=['GET'])
def listar_racas_inf(raca):
    start = time.time()
    graphs['c'].inc()

    cats = list(catCollection.find({"id": raca}))
    if (cats == []):
        response = Response(status=404)
        return response
    else:
        response = Response(status=200, headers={}, response=dumps(
            cats), mimetype='application/json')
        return response
    end = time.time()
    graphs['h'].observe(end - start)

### Listar raças partindo de um temperamento ###


@app.route('/listar-racas/temperamento/<string:temperamento>/', methods=['GET'])
def listar_racas_temperamento(temperamento):
    start = time.time()
    graphs['c'].inc()

    cats = list(catCollection.find({"temperament": {"$regex": temperamento}}))
    if (cats == []):
        response = Response(status=404)
        return response
    else:
        response = Response(status=200, headers={}, response=dumps(
            cats), mimetype='application/json')
        return response
    end = time.time()
    graphs['h'].observe(end - start)

### Listar raças partindo de uma origem ###


@app.route('/listar-racas/origem/<string:origem>/', methods=['GET'])
def listar_racas_origin(origem):
    start = time.time()
    graphs['c'].inc()
    cats = list(catCollection.find({"origin": origem}))
    if (cats == []):
        response = Response(status=404)
        return response
    else:
        response = Response(status=200, headers={}, response=dumps(
            cats), mimetype='application/json')
        return response
    end = time.time()
    graphs['h'].observe(end - start)

### Listar imagem de gatos com chapéu ###


@app.route('/listar/img/chapeu', methods=['GET'])
def listar_img_chapeu():
    start = time.time()
    graphs['c'].inc()
    cats = list(hatCatCollection.find())
    if (cats == []):
        response = Response(status=404)
        return response
    else:
        response = Response(status=200, headers={}, response=dumps(
            cats), mimetype='application/json')
        return response
    end = time.time()
    graphs['h'].observe(end - start)

### Listar imagem de gatos com óculus ###


@app.route('/listar/img/oculus', methods=['GET'])
def listar_img_oculus():
    start = time.time()
    graphs['c'].inc()
    cats = list(glassCatCollection.find())
    if (cats == []):
        response = Response(status=404)
    else:
        response = Response(status=200, headers={}, response=dumps(
            cats), mimetype='application/json')
        return response
    end = time.time()
    graphs['h'].observe(end - start)


@app.route('/insert')
def con():
    consummer.insertDatabse()
    return Response(status=201)


@app.route('/metrics')
def requests_count():
    res = []
    for k, v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res, mimetype="text/plain")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")