from flask import Flask

app = Flask(__name__)  #Instância com o nome do arquivo

@app.route('/')
def index():
    return "Hello World."


'''
No terminal:
Para indicar qual API será executada
$export FLASK_APP=hello.py

Para executar a API
#python3 -m flask run
'''

