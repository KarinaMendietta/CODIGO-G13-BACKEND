from flask import Flask,jsonify,request 
from pymongo import MongoClient 

cliente = MongoClient('mongodb://127.0.0.1')

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'status':True,
        'message':'Bienvenido a mi api mongoDB'
    })

@app.route('/alumno')
def getAlumno():
    
    return jsonify(context)

 

app.run(debug=True,port=5000)

    