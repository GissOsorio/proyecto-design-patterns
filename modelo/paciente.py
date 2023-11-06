from datetime import datetime

class Paciente:
    def __init__(self, nombre, fecha_nacimiento, tipo_identificacion, identificacion, contacto, apoderado=None):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.tipo_identificacion = tipo_identificacion
        self.identificacion = identificacion
        self.contacto = contacto
        self.apoderado = apoderado

    def paciente(self):
        return f"Paciente: {self.nombre}, {self.fecha_nacimiento}, {self.tipo_identificacion}, {self.identificacion}, {self.contacto.telefono}, {self.apoderado}"

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

    def tiene_apoderado(self):
        if self.apoderado:
            return True
        else:
            return False
