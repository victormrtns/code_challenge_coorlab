# encoding: utf-8
from flask import Flask,jsonify, request
from flask_cors import CORS
import json
import operator
import urllib
app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False
#Here you must to change the directory to works when you clone the repository
data_path = r"C:\Users\vmhug\OneDrive\Área de Trabalho\code-challenge-coorlab\code_challenge_coorlab\desafio_coorlab\app\data.json"
with open(data_path,encoding='utf-8') as myfile:
    data=json.load(myfile)

list_of_destinies = []

for i in data['transport']:
    list_of_destinies.append(i)
    
@app.route('/destinies',methods=['GET'])
def getdestinies():
    return jsonify(list_of_destinies)


@app.route('/travels',methods=['GET'])
def gettravels():
    body = request.args.get('city')
    output_dict = []
    for x in range(0, len(list_of_destinies)):
        if(list_of_destinies[x]['city'] == str(body)):
            output_dict.append(list_of_destinies[x])
    if(len(output_dict)==1):
        return jsonify(output_dict)
    else:
        #Initializing Values
        confortprice_duration = int(''.join(c for c in output_dict[0]['duration'] if c.isdigit()))
        economicprice = float(''.join(c for c in output_dict[0]['price_econ'] if (c.isdigit() or c =='.')))
        economicprice_travel = output_dict[0]
        confortprice_travel = output_dict[0]
        
        for x in range(0, len(output_dict)):
            formatted_value_economicprice = float(''.join(c for c in output_dict[x]['price_econ'] if (c.isdigit() or c =='.')))
            formatted_value_confortpriceduration = int(''.join(c for c in output_dict[x]['duration'] if c.isdigit()))
            
            print(economicprice)
            print(formatted_value_economicprice)
            
            if(formatted_value_confortpriceduration< confortprice_duration):
                confortprice_duration = formatted_value_confortpriceduration
                confortprice_travel = output_dict[x]
            
            if(economicprice> formatted_value_economicprice):
                economicprice = formatted_value_economicprice
                economicprice_travel = output_dict[x]
    return jsonify([confortprice_travel,economicprice_travel])

app.run(port=3000,host='localhost',debug=True)
