from modelo.persona import Persona
from datetime import datetime

class Paciente(Persona):
    def __init__(self, nombre, fecha_nacimiento, tipo_identificacion, identificacion, telefono = None, correo = None, apoderado = None):
        super().__init__(nombre, fecha_nacimiento, tipo_identificacion, identificacion, telefono = None, correo = None)
        
        if not self.es_mayor_de_edad():
            if apoderado is None:
                raise ValueError("Un paciente menor de edad debe tener un apoderado.")
            self.apoderado = apoderado
        else:
            self.apoderado = None

    def tiene_apoderado(self):
        if self.apoderado:
            return True
        else:
            return False
