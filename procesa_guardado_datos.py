import pymongo
from bson import ObjectId
from flask import Flask, jsonify

from clases.peticiones import PeticionDatos

app = Flask(__name__)
BATALLA = 1

client = pymongo.MongoClient("localhost", 27017)
db = client.DeathStar
collection_estrella = db["batalla{}".format(BATALLA)]


def procesar_guardado():
    peticion = PeticionDatos(BATALLA)
    for datos_tiempo_sensores in peticion.get_datos():
        print(datos_tiempo_sensores.tiempo)
        valores_sensores = []
        for sensores in datos_tiempo_sensores.sensores:
            valores_sensores.append(sensores.obtenerDatos())

        collection_estrella.insert_one({datos_tiempo_sensores.tiempo: valores_sensores})






procesar_guardado()
