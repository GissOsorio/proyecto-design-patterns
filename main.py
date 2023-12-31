from modelo.paciente import Paciente
from modelo.examen import Examen
from modelo.tipoExamen import TipoExamen
from modelo.apoderado import Apoderado
from modelo.fechaHoraExamen import FechaHoraExamen
from modelo.horarioAtencionLaboratorio import HorarioAtencionLaboratorio
from modelo.singletonFileReader import SingletonFileReader
from datetime import datetime

def main():
    FERIADOS = {"08-10", "11-03"} 
    HORARIO_APERTURA = "7:00"
    HORARIO_CIERRE = "16:00"
    HORARIO_APERTURA_EARLY = "7:00"
    HORARIO_CIERRE_EARLY = "9:00"
    DIAS_ATENCION = [0,1,2,3,4]
    nombre_archivo = 'inputs/lab_input.txt'
    horario_atencion_laboratorio = crear_horario_atencion_laboratorio(DIAS_ATENCION, HORARIO_APERTURA, HORARIO_CIERRE, FERIADOS)
    lineas_del_archivo = leer_datos_desde_archivo(nombre_archivo)
    examenes = leer_examenes_desde_lineas_del_archivo(lineas_del_archivo, horario_atencion_laboratorio)
    imprimir_listado_examenes(examenes)

def crear_horario_atencion_laboratorio(dias_semana, HORARIO_APERTURA, HORARIO_CIERRE, dias_feriados):
    horario_apertura = datetime.strptime(HORARIO_APERTURA, "%H:%M").time()
    horario_cierre = datetime.strptime(HORARIO_CIERRE, "%H:%M").time()
    horario_atencion_laboratorio = HorarioAtencionLaboratorio(dias_semana, horario_apertura, horario_cierre, dias_feriados)
    return horario_atencion_laboratorio

def leer_datos_desde_archivo(nombre_archivo):
    singleton_file_reader = SingletonFileReader(nombre_archivo)
    lineas = singleton_file_reader.read_lines()
    return lineas

def leer_examenes_desde_lineas_del_archivo(lineas, horario_atencion_laboratorio):
    examenes = []
    for linea in lineas:
        partes = linea.strip().split('|')
        if len(partes) == 1:
            fecha_actual = partes[0]
        elif len(partes) == 10 or len(partes) == 15:
            try:
                tipoExamen = leer_tipo_examen(partes)
                fecha_hora_examen = revisar_fecha(partes, fecha_actual)
                apoderado = leer_apoderado(partes)
                paciente = leer_paciente(partes, apoderado)
                examenes = agregar_examen_a_examenes("guardado", paciente, fecha_hora_examen, examenes, tipoExamen, horario_atencion_laboratorio)
            except ValueError as e:
                print(f"Cita Existente con formato equivocado - Error: {e}")
        elif len(partes) == 11 or len(partes) == 16:
            try:
                tipoExamen = agregar_tipo_examen(partes)
                fecha_hora_examen = agregar_fecha(partes)
                apoderado = agregar_apoderado(partes)
                paciente = agregar_paciente(partes, apoderado)
                examenes = agregar_examen_a_examenes("nuevo", paciente, fecha_hora_examen, examenes, tipoExamen, horario_atencion_laboratorio)
            except ValueError as e:
                print(f"No se pudo agregar - Error: {e}")

    return examenes

def agregar_examen_a_examenes(estado, paciente, fecha_hora_examen, examenes, tipoExamen, horario_atencion_laboratorio):
    fecha = FechaHoraExamen(fecha_hora_examen, horario_atencion_laboratorio)
    validar_cita_paciente(paciente, fecha_hora_examen, examenes)
    validar_citas_simultaneas(fecha_hora_examen, examenes)
    fecha.verificar_restricciones()
    examen = agregar_examen(paciente, tipoExamen, fecha.fecha_hora_examen)
    examen.cambiar_estado(estado)
    examen.contexto.estado.realizar_examen()
    examenes.append(examen)
    return examenes

def validar_citas_simultaneas(fecha_hora_nuevo_examen, examenes):
    contador = 1
    for examen in examenes:
        if fecha_hora_nuevo_examen.date() == examen.fecha_hora_examen.date() and fecha_hora_nuevo_examen.time() == examen.fecha_hora_examen.time():
            contador += 1
            
    if contador > 2:
        raise ValueError("Se pueden hacer hasta 2 reservas en el mismo horario")
    

def validar_cita_paciente(paciente, fecha_hora_nuevo_examen, examenes):
    for examen in examenes:
        if examen.paciente.identificacion == paciente.identificacion and examen.fecha_hora_examen.date() == fecha_hora_nuevo_examen.date() and examen.fecha_hora_examen.time() == fecha_hora_nuevo_examen.time():
            raise ValueError("El paciente ya tiene una cita en el mismo horario.")

def leer_apoderado(partes):
    if len(partes) == 15:
        _, _, _, _, _, _, _, _, _, _, nombre_apoderado, tipo_identificacion_apoderado, identificacion_apoderado, fecha_nacimiento_apoderado, _ = partes
        return crear_objeto_apoderado(nombre_apoderado, tipo_identificacion_apoderado, identificacion_apoderado, fecha_nacimiento_apoderado)

    return None

def agregar_apoderado(partes):
    if len(partes) == 16:
        _, _, _, _, _, _, _, _, _, _, _, nombre_apoderado, tipo_identificacion_apoderado, identificacion_apoderado, fecha_nacimiento_apoderado, _ = partes
        return crear_objeto_apoderado(nombre_apoderado, tipo_identificacion_apoderado, identificacion_apoderado, fecha_nacimiento_apoderado)

    return None
    
def crear_objeto_apoderado(nombre_apoderado, tipo_identificacion_apoderado, identificacion_apoderado, fecha_nacimiento_apoderado):
    return Apoderado(nombre_apoderado, parsear_fecha(fecha_nacimiento_apoderado), tipo_identificacion_apoderado, identificacion_apoderado)
    
def leer_paciente(partes, apoderado):
    correo_contacto = "dummy@hotmail.com"
    if len(partes) == 10:
        _, _, _, nombre_paciente, _, tipo_identificacion_paciente, identificacion_paciente, telefono_contacto, fecha_nacimiento_paciente, _= partes
        return crear_objeto_paciente(nombre_paciente, fecha_nacimiento_paciente, tipo_identificacion_paciente, identificacion_paciente, telefono_contacto, correo_contacto)
    elif len(partes) == 15:
        _, _, _, nombre_paciente, _, tipo_identificacion_paciente, identificacion_paciente, telefono_contacto, fecha_nacimiento_paciente, _, _ ,_ ,_ ,_, _ = partes
        return crear_objeto_paciente_con_apoderado(nombre_paciente, fecha_nacimiento_paciente, tipo_identificacion_paciente, identificacion_paciente, telefono_contacto, correo_contacto, apoderado)
    else:
        return None

def agregar_paciente(partes, apoderado):
    correo_contacto = "dummy@hotmail.com"
    if len(partes) == 11:
        _, _, _, _, nombre_paciente, rango_edad_paciente, tipo_identificacion_paciente, identificacion_paciente, telefono_contacto, fecha_nacimiento_paciente, _= partes
        return crear_objeto_paciente(nombre_paciente, fecha_nacimiento_paciente, tipo_identificacion_paciente, identificacion_paciente, telefono_contacto, correo_contacto)
    elif len(partes) == 16:
        _, _, _, _, nombre_paciente, rango_edad_paciente, tipo_identificacion_paciente, identificacion_paciente, telefono_contacto, fecha_nacimiento_paciente, _, _ ,_ ,_ ,_, _ = partes
        return crear_objeto_paciente_con_apoderado(nombre_paciente, fecha_nacimiento_paciente, tipo_identificacion_paciente, identificacion_paciente, telefono_contacto, correo_contacto, apoderado)
    else:
        return None

def crear_objeto_paciente(nombre_paciente, fecha_nacimiento_paciente, tipo_identificacion_paciente, identificacion_paciente, telefono_contacto, correo_contacto):
    return Paciente(nombre_paciente, parsear_fecha(fecha_nacimiento_paciente), tipo_identificacion_paciente, identificacion_paciente, telefono_contacto, correo_contacto)

def crear_objeto_paciente_con_apoderado(nombre_paciente, fecha_nacimiento_paciente, tipo_identificacion_paciente, identificacion_paciente, telefono_contacto, correo_contacto, apoderado):
    return Paciente(nombre_paciente, parsear_fecha(fecha_nacimiento_paciente), tipo_identificacion_paciente, identificacion_paciente, telefono_contacto, correo_contacto, apoderado)


def leer_tipo_examen(partes):
    if len(partes) == 10:
        _, nombre_examen, horario_especial_examen, _, _, _, _, _, _, _ = partes
        tipoExamen = TipoExamen(nombre_examen, horario_especial_examen)
        return tipoExamen
    elif len(partes) == 15:
        _, nombre_examen, horario_especial_examen, _, _, _, _, _, _, _, _, _, _, _, _ = partes
        tipoExamen = TipoExamen(nombre_examen, horario_especial_examen)
        return tipoExamen
    else:
        return None

def agregar_tipo_examen(partes):
    if len(partes) == 11:
        _, _, nombre_examen, horario_especial_examen, _, _, _, _, _, _, _ = partes
        tipoExamen = TipoExamen(nombre_examen, horario_especial_examen)
        return tipoExamen
    elif len(partes) == 16:
        _, _, nombre_examen, horario_especial_examen, _, _, _, _, _, _, _, _, _, _, _, _ = partes
        tipoExamen = TipoExamen(nombre_examen, horario_especial_examen)
        return tipoExamen
    else:
        return None

def revisar_fecha(partes, fecha_actual):
    if len(partes) == 10:
        hora_examen, _, _, _, _, _, _, _, _, _ = partes
        fecha_hora_examen = combinar_fecha_hora(fecha_actual, hora_examen)
        return fecha_hora_examen
    elif len(partes) == 15:
        hora_examen, _, _, _, _, _, _, _, _, _, _, _, _, _, _ = partes
        fecha_hora_examen = combinar_fecha_hora(fecha_actual, hora_examen)
        return fecha_hora_examen
    else:
        return None

def agregar_fecha(partes):
    if len(partes) == 11:
        fecha_examen, hora_examen, _, _, _, _, _, _, _, _, _ = partes
    elif len(partes) == 16:
        fecha_examen, hora_examen, _, _, _, _, _, _, _, _, _, _, _, _, _, _ = partes
    
    return combinar_fecha_hora(fecha_examen, hora_examen)

def agregar_examen(paciente, tipoExamen, fecha_hora_examen):
    examen = Examen(paciente, tipoExamen, fecha_hora_examen)
    return examen

def parsear_fecha(textoFecha):
    try:
        return datetime.strptime(textoFecha, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Fecha AAAA-MM-DD incorrecta")

def combinar_fecha_hora(fecha_string, hora_string):
    if not fecha_string or not hora_string:
        raise ValueError("Fecha vacía")
    try:
        hora = datetime.strptime(hora_string, '%H:%M')
        fecha = datetime.strptime(fecha_string, '%Y-%m-%d')
        return datetime(year=fecha.year, month=fecha.month, day=fecha.day, hour=hora.hour, minute=hora.minute)
    except ValueError:
        raise ValueError("Fecha incorrecta")

def leer_fechas_examenes(examenes):
    examenes_por_fecha = {}
    for examen in examenes:
        fecha = examen.fecha_hora_examen.date()
        if fecha not in examenes_por_fecha:
            examenes_por_fecha[fecha] = []
        examenes_por_fecha[fecha].append(examen)
    
    return examenes_por_fecha

def imprimir_listado_examenes(examenes):
    examenes.sort(key=lambda x: x.fecha_hora_examen)
    examenes_por_fecha = leer_fechas_examenes(examenes)
    for fecha, ex_list in examenes_por_fecha.items():
        print(fecha)
        for examen in ex_list:
            if examen.paciente.tiene_apoderado():
                examen.imprimir_examen_persona_menor_de_edad()
            else:
                examen.imprimir_examen_persona_mayor_de_edad()
        print()

if __name__ == "__main__":
    main()