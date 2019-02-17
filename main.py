import smartcar
from flask import Flask, redirect, request, jsonify
from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET', 'POST'])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        response = jsonify({'you sent': some_json})
        return response, 201
    else:
        response = jsonify({"about":"Hello World!"})
        return jsonify({"about":"Hello World!"})