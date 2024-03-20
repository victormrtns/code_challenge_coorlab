from flask import Flask,jsonify, request
import json
import operator
app = Flask(__name__)
#Here you must to change the directory to works when you clone the repository
data_path = r"C:\Users\vmhug\OneDrive\Área de Trabalho\code-challenge-coorlab\code_challenge_coorlab\desafio_coorlab\app\data.json"
with open(data_path, 'r') as myfile:
    data=json.load(myfile)

list_of_destinies = []

for i in data['transport']:
    list_of_destinies.append(i)
    
@app.route('/destinies',methods=['GET'])
def getdestinies():
    return jsonify(list_of_destinies)


@app.route('/travels',methods=['GET'])
def gettravels():
    args = list(request.args)
    output_dict = []
    for x in range(0, len(list_of_destinies)):
        if(list_of_destinies[x]['city'] == str(args[0])):
            output_dict.append(list_of_destinies[x])
    return jsonify(output_dict)

app.run(port=5000,host='localhost',debug=True)
