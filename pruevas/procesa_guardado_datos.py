import pymongo
from bson import ObjectId
from flask import Flask, jsonify

from clases.peticiones import PeticionDatos

app = Flask(__name__)

client = pymongo.MongoClient("localhost", 27017)
db = client.estrella
collection_estrella = db["estrella"]


def getID(tiempos_sensores):
    documentos = collection_estrella.find({
        str(tiempos_sensores.tiempo.year): {
            str(tiempos_sensores.tiempo.month): {
                str(tiempos_sensores.tiempo.day): {
                    str(tiempos_sensores.tiempo.hour): {
                        str(tiempos_sensores.tiempo.minute): {

                        }
                    }
                }
            }
        }
    })
    if documentos[0] is not None:
        return documentos[0]['_id']


def procesar_guardado():
    peticion = PeticionDatos(2)
    for tiempos_sensores in peticion.get_datos():
        valores_sensores = []
        for sensores in tiempos_sensores.sensores:
            valores_sensores.append(sensores.obtenerDatos())

        print(tiempos_sensores.tiempo)
        num_registros = collection_estrella.count_documents({

            str(tiempos_sensores.tiempo.year): {
                str(tiempos_sensores.tiempo.month): {
                    str(tiempos_sensores.tiempo.day): {
                        str(tiempos_sensores.tiempo.hour): {
                                str(tiempos_sensores.tiempo.minute): {

                            }
                        }
                    }
                }
            }})
        print(num_registros)
        if num_registros == 0:
            db.estrella.insert_one({
                str(tiempos_sensores.tiempo.year): {
                    str(tiempos_sensores.tiempo.month): {
                        str(tiempos_sensores.tiempo.day): {
                            str(tiempos_sensores.tiempo.hour): {
                                str(tiempos_sensores.tiempo.minute): {

                                }
                            }
                        }
                    }
                }})
        else:

            object_id = getID(tiempos_sensores)
            collection_estrella.update_one(
                {'_id': ObjectId(object_id)}, {
                    '$set': {
                        str(tiempos_sensores.tiempo.year): {
                            str(tiempos_sensores.tiempo.month): {
                                str(tiempos_sensores.tiempo.day): {
                                    str(tiempos_sensores.tiempo.hour): {
                                        str(tiempos_sensores.tiempo.minute): valores_sensores

                                    }
                                }
                            }
                        }
                    }

                })


# print(getID())
procesar_guardado()
