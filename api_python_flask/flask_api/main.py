from flask import Flask, jsonify
from flask import request
from app.models import Application as App

app = Flask(__name__)  #Instância com o nome do arquivo


'''
GET com parâmetros
URL: http://127.0.0.1:5000/search?name=John&location=Miami
'''
@app.route('/search', methods=['GET'])
def search():
    args = request.args
    return args

@app.route('/filter', methods=['GET'])
def ffilter():
    app = App()
    args = request.args
    print(args)
    filter = app.check(args["name"])   #O request pode ser tratado como um dicionário chave-valor
    return filter


'''
Método POST
URL: http://127.0.0.1:5000/json_example
Body:
{
    "name" : "John",
    "age" : "5"
}
'''
@app.route('/json_example', methods=['POST'])
def request_json():
    data = request.json
    print(data.get('name'))  #Imprime no terminal onde o servidor está rodando
    print(data.get('age'))
    print(data)
    print(type(data))
    return data


'''
Método DELETE
URL Exemplo: http://127.0.0.1:5000/delete/user/054
'''
@app.route("/delete/user/<id>", methods=["DELETE"])
def request_delete(id):
    app = App()
    value = app.clear(id)
    data = jsonify({"deleted":value})  #Retorna o JSON formatado
    return data


'''
Método PUT
URL exemplo: http://127.0.0.1:5000/user/modify/643
Body JSON format:
{
    "name" : "John",
    "age" : "5"
}
'''
@app.route('/user/modify/<id>', methods=['PUT'])
def request_put(id):
    app = App()
    print("The id is: ", id)
    data = request.json
    print(data.get('name'))
    print(data.get('age'))
    print(data)
    #Put App method here
    return data


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

'''
Executar a API
#python3 main.py
'''
