from datetime import datetime

class Fecha:
    FERIADOS = {"08-11", "11-03"} 
    HORARIO_APERTURA = "7:00"
    HORARIO_CIERRE = "16:00"
    HORARIO_APERTURA_EARLY = "7:00"
    HORARIO_CIERRE_EARLY = "9:00"
    DIAS_ATENCION = [0,1,2,3,4]

    def __init__(self, fecha_hora_examen):
        if not self.es_dia_laborable(fecha_hora_examen):
            raise ValueError("El establecimiento solo opera de lunes a viernes from FECHA.")

        if not self.es_hora_laborable(fecha_hora_examen):
            raise ValueError("El establecimiento solo opera de 7:00 a 16:00.")
        
        if self.es_feriado(fecha_hora_examen):
            raise ValueError("El establecimiento no opera en feriados.")

        if not self.es_intervalo_de_cita_valido(fecha_hora_examen):
            raise ValueError("La hora del examen debe ser en intervalos de 20 minutos.")
            
        self.fecha_hora_examen = fecha_hora_examen

    def es_dia_laborable(self, fecha):
        numero_dia_semana = fecha.weekday()
        return numero_dia_semana in self.DIAS_ATENCION

    def es_hora_laborable(self, fecha_hora):
        hora_apertura = datetime.strptime(self.HORARIO_APERTURA, "%H:%M").time()
        hora_cierre = datetime.strptime(self.HORARIO_CIERRE, "%H:%M").time()
        hora_examen = fecha_hora.hour
        return hora_examen >= hora_apertura.hour and hora_examen < hora_cierre.hour

    def es_hora_especial(self, fecha_hora):
        hora_apertura = datetime.strptime(self.HORARIO_APERTURA_EARLY, "%H:%M").time()
        hora_cierre = datetime.strptime(self.HORARIO_CIERRE_EARLY, "%H:%M").time()
        hora_examen = fecha_hora.hour
        return hora_examen >= hora_apertura.hour and hora_examen < hora_cierre.hour

    def es_feriado(self, fecha_hora):
        fecha_formateada = fecha_hora.strftime("%d-%m")
        return fecha_formateada in self.FERIADOS

    def es_intervalo_de_cita_valido(self, fecha_hora):
        minutos_examen = fecha_hora.minute
        return minutos_examen % 20 == 0

    def es_fecha_futura(self, fecha_hora):
        ahora = datetime.now()
        return fecha_hora > ahora