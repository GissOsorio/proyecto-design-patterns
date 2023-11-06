from datetime import datetime

class Examen:
    def __init__(self, paciente, tipo_examen, fecha_hora_examen):
        self.paciente = paciente
        self.tipo_examen = tipo_examen
        self.fecha_hora_examen = fecha_hora_examen


    def examen(self):
        return f"Examen: {self.paciente.nombre}, {self.tipo_examen.nombre}, {self.fecha_hora_examen}"
