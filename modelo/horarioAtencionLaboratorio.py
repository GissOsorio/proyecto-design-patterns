from datetime import datetime

class HorarioAtencionLaboratorio:
    def __init__(self, dias_semana, horario_apertura, horario_cierre, dias_feriados):
        self.dias_semana = dias_semana
        self.horario_apertura = horario_apertura
        self.horario_cierre = horario_cierre
        self.dias_feriados = dias_feriados

    def es_dia_laborable(self, fecha):
        return fecha.weekday() in self.dias_semana

    def es_hora_laborable(self, fecha_hora):
        return fecha_hora.hour >= self.horario_apertura.hour and fecha_hora.hour < self.horario_cierre.hour

    # def es_hora_especial(self, fecha_hora):
    #     hora_apertura = datetime.strptime(self.HORARIO_APERTURA_EARLY, "%H:%M").time()
    #     hora_cierre = datetime.strptime(self.HORARIO_CIERRE_EARLY, "%H:%M").time()
    #     hora_examen = fecha_hora.hour
    #     return hora_examen >= hora_apertura.hour and hora_examen < hora_cierre.hour

    def es_feriado(self, fecha_hora):
        fecha_formateada = fecha_hora.strftime("%m-%d")
        return fecha_formateada in self.dias_feriados

    def es_intervalo_de_cita_valido(self, fecha_hora):
        minutos_examen = fecha_hora.minute
        return minutos_examen % 20 == 0

    # def es_fecha_futura(self, fecha_hora):
    #     ahora = datetime.now()
    #     return fecha_hora > ahora
