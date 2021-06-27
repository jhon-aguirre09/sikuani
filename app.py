from flask import Flask, request
from clases.peticiones import PeticionDatos
import pymongo


app = Flask(__name__)

peticion = PeticionDatos()

@app.route('/', methods=['GET', 'POST'])
def hello():

    if request.method == 'GET':
        peticion.init_request()
        client = pymongo.MongoClient("mongodb+srv://new_user:sikuani@cluster0.vxniy.mongodb.net/sikuanidb?retryWrites=true&w=majority") 
        db = client.test
        return str(db)
        
    if request.method == 'POST':
        data = request.get_json()
        peticion.get_datos(data)
        print(data["data"])
        return data
