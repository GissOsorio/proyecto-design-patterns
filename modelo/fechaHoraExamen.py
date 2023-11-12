from datetime import datetime

class FechaHoraExamen:

    def __init__(self, fecha_hora_examen, horario_atencion_laboratorio):
        self.fecha_hora_examen = fecha_hora_examen
        self.horario_atencion_laboratorio = horario_atencion_laboratorio
    
    def verificar_restricciones(self):
        if not self.horario_atencion_laboratorio.es_dia_laborable(self.fecha_hora_examen):
            raise ValueError("El establecimiento solo opera de lunes a viernes.")

        if not self.horario_atencion_laboratorio.es_hora_laborable(self.fecha_hora_examen):
            raise ValueError("El establecimiento solo opera de 7:00 a 16:00.")
        
        if self.horario_atencion_laboratorio.es_feriado(self.fecha_hora_examen):
            raise ValueError("El establecimiento no opera en feriados.")

        if not self.horario_atencion_laboratorio.es_intervalo_de_cita_valido(self.fecha_hora_examen):
            raise ValueError("La hora del examen debe ser en intervalos de 20 minutos.")
            