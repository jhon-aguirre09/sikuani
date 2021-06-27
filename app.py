from flask import Flask, request
from clases.peticiones import PeticionDatos
import pymongo


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():

    # peticion = PeticionDatos()

    if request.method == 'GET':
        client = pymongo.MongoClient("mongodb+srv://new_user:sikuani@cluster0.vxniy.mongodb.net/sikuanidb?retryWrites=true&w=majority") 
        db = client.test
        return str(db)
        
    if request.method == 'POST':
        request_data = request.json()
        return "<h1>Bienvenido " + request_data + "</h1>"

    # def show_data():
    #     return peticion