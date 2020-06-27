from flask import Flask, jsonify

app = Flask("API-CAT")


@app.route('/', methods=['GET'])
def home():
    return "API-CAT", 200


@app.route('/listar-racas', methods=['GET'])
def listar_racas():
    return jsonify(), 200


if __name__ == '__main__':
    app.run(debug=True)
