import smartcar
from flask import Flask, redirect, request, jsonify
from flask_cors import CORS

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Smartcar App Dependencies Installed</h1>'