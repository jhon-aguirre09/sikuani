import time
import pymongo

from flask import Flask
import datetime

app = Flask(__name__)
starttime = time.time()
BATALLA = 1

client = pymongo.MongoClient("localhost", 27017)
db = client.DeathStar
collection_estrella = db["batalla{}".format(BATALLA)]



def get_primera_fecha():
    datos = collection_estrella.find().limit(1)
    try:
        #print(datos[0]['tiempo'])
        #print(list(datos[0].keys()))
        return datos[0]['tiempo']
    except:
        return None


def analizar_datos_30sec():
    fecha_proceso = get_primera_fecha()
    procesar = False
    if fecha_proceso is not None:
        procesar = True
        fecha_proceso = datetime.datetime.strptime(fecha_proceso, '%Y-%m-%d %H:%M:%S')

    else:
        print("No se procesarar datos por la inexistencia de los mismos")
    while procesar:
        datos = collection_estrella.find({"tiempo": fecha_proceso.strftime("%Y-%m-%d %H:%M:%S")})
        try:
            print(datos[0])
            time.sleep(1.0 - ((time.time() - starttime) % 1.0))
            added_seconds = datetime.timedelta(0, 1)
            fecha_proceso = fecha_proceso + added_seconds
        except:
            print("No hay mas documentos")
            break




analizar_datos_30sec()