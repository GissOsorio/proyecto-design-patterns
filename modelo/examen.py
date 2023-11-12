from datetime import datetime
from modelo.paciente import Paciente
from modelo.examenContexto import ExamenContexto

class Examen:
    HORARIO_APERTURA_EARLY = "7:00"
    HORARIO_CIERRE_EARLY = "9:00"

    def __init__(self, paciente, tipo_examen, fecha_hora_examen):
        if paciente is None or fecha_hora_examen is None or tipo_examen is None:
            raise ValueError("Error: Faltan datos.")

        if tipo_examen.horario == "EARLY" and not self.es_hora_especial(fecha_hora_examen):
            raise ValueError("Este tipo de examen solo puede ser realizado en el horario de 7:00 a 9:00.")

        self.contexto = ExamenContexto(self)
        self.paciente = paciente
        self.tipo_examen = tipo_examen
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

    def es_hora_especial(self, fecha_hora):
        hora_apertura = datetime.strptime(self.HORARIO_APERTURA_EARLY, "%H:%M").time()
        hora_cierre = datetime.strptime(self.HORARIO_CIERRE_EARLY, "%H:%M").time()
        hora_examen = fecha_hora.hour
        return hora_examen >= hora_apertura.hour and hora_examen < hora_cierre.hour

    def es_fecha_futura(self, fecha_hora):
        ahora = datetime.now()
        return fecha_hora > ahora