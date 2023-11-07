from datetime import datetime

class Dia:
    def __init__(self, dia, horario):
        self.dia = dia
        self.horario = horario

    def horario(self):
        return f"Dia: {self.dia}, {self.horario}"
        