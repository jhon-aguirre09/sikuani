from datetime import datetime

class TiempoSegundos:

    def __init__(self, tiempo, sensores):
        # self.tiempo = datetime.strptime(tiempo, '%Y-%m-%d %H:%M:%S')
        self.tiempo = tiempo
        self.sensores = sensores # array de sensores