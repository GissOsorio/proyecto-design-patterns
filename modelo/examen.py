from datetime import datetime
from modelo.paciente import Paciente

class Examen:
    FERIADOS = {"08-11", "11-03"} 
    HORARIO_APERTURA = "7:00"
    HORARIO_CIERRE = "16:00"
    HORARIO_APERTURA_EARLY = "7:00"
    HORARIO_CIERRE_EARLY = "9:00"
    DIAS_ATENCION = [0,1,2,3,4]

    def __init__(self, paciente, tipo_examen, fecha_hora_examen, estado = None):
        if paciente is None:
            raise ValueError("Error: Se requiere un paciente para crear un examen.")

        self.paciente = paciente
        self.tipo_examen = tipo_examen
        self.estado = estado

        if estado == "nuevo" and not self.es_fecha_futura(fecha_hora_examen):
            raise ValueError("La fecha del examen debe ser en el futuro cuando es una nueva cita.")

        if tipo_examen.horario == "EARLY" and not self.es_hora_especial(fecha_hora_examen):
            raise ValueError("Este tipo de examen solo puede ser realizado en el horario de 7:00 a 9:00.")

        self.fecha_hora_examen = fecha_hora_examen

    def imprimir_examen_persona_mayor_de_edad(self):
        hora_examen = self.fecha_hora_examen.strftime("%H:%M")
        nombre_examen = self.tipo_examen.nombre
        horario_especial_examen = self.tipo_examen.horario
        nombre_paciente = self.paciente.nombre
        rango_edad_paciente = self.paciente.obtener_rango_edad()
        tipo_identificacion_paciente = self.paciente.tipo_identificacion
        identificacion_paciente = self.paciente.identificacion
        telefono_contacto = self.paciente.telefono
        fecha_nacimiento_paciente = self.paciente.fecha_nacimiento.strftime('%Y-%m-%d')
        print(f"{hora_examen}|{nombre_examen}|{horario_especial_examen}|{nombre_paciente}|{rango_edad_paciente}|{tipo_identificacion_paciente}|{identificacion_paciente}|{telefono_contacto}|{fecha_nacimiento_paciente}|") 


    def imprimir_examen_persona_menor_de_edad(self):
        hora_examen = self.fecha_hora_examen.strftime("%H:%M")
        nombre_examen = self.tipo_examen.nombre
        horario_especial_examen = self.tipo_examen.horario
        nombre_paciente = self.paciente.nombre
        rango_edad_paciente = self.paciente.obtener_rango_edad()
        tipo_identificacion_paciente = self.paciente.tipo_identificacion
        identificacion_paciente = self.paciente.identificacion
        telefono_contacto = self.paciente.telefono
        fecha_nacimiento_paciente = self.paciente.fecha_nacimiento.strftime('%Y-%m-%d')
        es_apoderado = "APO"
        nombre_apoderado = self.paciente.apoderado.nombre
        tipo_identificacion_apoderado = self.paciente.apoderado.tipo_identificacion
        identificacion_apoderado = self.paciente.apoderado.identificacion
        fecha_nacimiento_apoderado = self.paciente.apoderado.fecha_nacimiento.strftime('%Y-%m-%d')
        print(f"{hora_examen}|{nombre_examen}|{horario_especial_examen}|{nombre_paciente}|{rango_edad_paciente}|{tipo_identificacion_paciente}|{identificacion_paciente}|{telefono_contacto}|{fecha_nacimiento_paciente}|{es_apoderado}|{nombre_apoderado}|{tipo_identificacion_apoderado}|{identificacion_apoderado}|{fecha_nacimiento_apoderado}|") 

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
        fecha_formateada = fecha_hora.strftime("%m-%d")
        return fecha_formateada in self.FERIADOS

    def es_intervalo_de_cita_valido(self, fecha_hora):
        minutos_examen = fecha_hora.minute
        return minutos_examen % 20 == 0

    def es_fecha_futura(self, fecha_hora):
        ahora = datetime.now()
        return fecha_hora > ahora