from modelo.persona import Persona
from datetime import datetime

class Apoderado(Persona):
    def __init__(self, nombre, fecha_nacimiento, tipo_identificacion, identificacion, telefono = None, correo = None):
        super().__init__(nombre, fecha_nacimiento, tipo_identificacion, identificacion, telefono = None, correo = None)
        
        if not self.es_mayor_de_edad():
            raise ValueError("El apoderado debe ser mayor de edad.")
