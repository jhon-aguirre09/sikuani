import json
import requests

from clases.sensor import Sensor
from clases.tiempo_segundos import TiempoSegundos


class PeticionDatos:
    def __init__(self):
        # self.url = 'http://ec2-100-26-152-194.compute-1.amazonaws.com:3000/battles/{}'.format(batalla)
        self.url = 'http://ec2-100-26-152-194.compute-1.amazonaws.com:3000/battles/2/faucet'
        self.datos = {'Token': '11360e9d-0fdc-49d4-b127-aec80336c6a9', 'content-type': 'application/json'}
        self.respuesta = requests.get(self.url, headers=self.datos)
        # self.res_json = self.respuesta.json()

    def get_datos(self):
        self.lista_tiempos = []
        for datos in self.res_json['data']:
            tiempo_datos = datos.split(',')
            tiempo = tiempo_datos[0]
            contador = 0
            # print("Para el tiempo: ", tiempo)
            lista_sensores = []
            for sensor_tiempo in tiempo_datos:
                if contador != 0:
                    sensor_info_array = sensor_tiempo.replace('(', '').replace(')', '').split('|')
                    lista_sensores.append(Sensor(sensor_info_array[0], sensor_info_array[1]))
                else:
                    contador += 1
            self.lista_tiempos.append(TiempoSegundos(tiempo, lista_sensores))
        return self.lista_tiempos

