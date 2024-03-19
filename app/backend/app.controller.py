from flask import Flask,jsonify, request
import json
app = Flask(__name__)
#Here you must to change the directory to works when you clone the repository
data_path = r"C:\Users\vmhug\OneDrive\Área de Trabalho\code-challenge-coorlab\code_challenge_coorlab\desafio_coorlab\app\data.json"
with open(data_path, 'r') as myfile:
    data=myfile.read()
data_json = json.loads(data)
