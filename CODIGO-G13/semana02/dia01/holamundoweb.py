from unittest import result
from flask import Flask, request

#creamos objeto de la clase Flask
app = Flask(__name__)

#creamos mi primer ruta
@app.route('/')
def index():
    return '<center><h1>HOLA MUNDO FLASK</h1></center>'

@app.route('/saludo')
def saludo():
    nombre = request.args.get('nombre','no hay nombre')
    return '<center><b>Hola {}</b><center>'.format(nombre)

@app.route('/suma')
def suma():
    n1 = request.args.get('n1','0')
    n2 = request.args.get('n2','0')
    resultado = int(n1) + int(n2)
    return '<center><b>la suma de {} + {} es {}</b><center>'.format(n1,n2,resultado)
    #/suma?n1=20&n2=10 asi lo puse en el puerto 5000

@app.route('/resta/<int:n1>/<int:n2>')
def resta(n1=0,n2=0):
    resultado = n1 - n2
    return '<center><b>la resta de {} - {} es {}</b><center>'.format(n1,n2,resultado)
    #/resta/2/4 asi lo puse en el puerto 5000
    
#desplegamos nuestra app web
app.run(debug = True) #run despliega una aplicacion web

