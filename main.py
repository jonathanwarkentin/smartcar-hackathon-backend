import smartcar
from flask import Flask, redirect, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET', 'POST'])
@cross_origin(origin='https://shrouded-ravine-72981.herokuapp.com/',headers=['Content- Type','Authorization'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        response = jsonify({'you sent': some_json})
        return response, 201
    else:
        response = jsonify({"about":"Hello World!"})
        return jsonify({"about":"Hello World!"})