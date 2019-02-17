import smartcar
from flask import Flask, redirect, request, jsonify
from flask_cors import CORS

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        response = jsonify({'you sent': some_json})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 201
    else:
        response = jsonify({"about":"Hello World!"})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return jsonify({"about":"Hello World!"})