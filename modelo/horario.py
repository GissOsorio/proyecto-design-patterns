from datetime import datetime

class Horario:
    def __init__(self, horario_apertura, horario_cierre):
        self.horario_apertura = horario_apertura
        self.horario_cierre = horario_cierre

    def horario(self):
        return f"Horario: {self.horario_apertura}, {self.horario_apertura}"
