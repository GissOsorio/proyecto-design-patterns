from datetime import datetime

class HorarioLaboratorio:
    def __init__(self, dias_semana, horario_apertura, horario_cierre, dias_feriados):
        self.dias_semana = dias_semana
        self.horario_apertura = horario_apertura
        self.horario_cierre = horario_cierre
        self.dias_feriados = dias_feriados

    def horario(self):
        return f"Horario: {self.horario_apertura}, {self.horario_apertura}"
