from datetime import datetime

class Persona:
    def __init__(self, nombre, fecha_nacimiento, tipo_identificacion, identificacion, telefono = None, correo = None):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.tipo_identificacion = tipo_identificacion
        self.identificacion = identificacion
        self.telefono = telefono
        self.correo = correo


    def es_mayor_de_edad(self):
        fecha_actual = datetime.now()
        edad = fecha_actual.year - self.fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        if edad >= 18:
            return True
        else:
            return False

    def obtener_rango_edad(self):
        if self.es_mayor_de_edad():
            return "ADULTO"
        else:
            return "PMENOR"

