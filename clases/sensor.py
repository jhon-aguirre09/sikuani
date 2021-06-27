class Sensor:
    def __init__(self, nave, magtos):
        self.tipo_nave = nave # 'Starfighter','Bomber','Scout vessel','Gunship', '-'
        self.magtos = int(magtos)

        self.activo = True
        self.enemigo = False
        if self.magtos > 100:
            self.enemigo = True
        elif magtos == 0:
            self.activo = False

    def obtenerDatos(self):

        return [self.tipo_nave, self.magtos]