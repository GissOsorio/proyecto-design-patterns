from datetime import datetime

class Paciente:
    def __init__(self, nombre, fecha_nacimiento, tipo_identificacion, identificacion):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.tipo_identificacion = tipo_identificacion
        self.identificacion = identificacion

    def paciente(self):
        return f"Paciente: {self.nombre}, {self.fecha_nacimiento}, {self.tipo_identificacion}, {self.identificacion}"

    def esMayorDeEdad(self):
        fecha_actual = datetime.now()
        edad = fecha_actual.year - self.fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        if edad >= 18:
            return True
        else:
            return False
