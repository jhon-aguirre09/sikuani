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
        data = request.POST.json()
        print(request.jsonify(data))
        return "Bienvenido"

    # def show_data():
    #     return peticion