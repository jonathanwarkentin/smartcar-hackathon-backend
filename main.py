import smartcar
from flask import Flask, redirect, request, jsonify
from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/": {"origins": "https://shrouded-ravine-72981.herokuapp.com/"}})

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