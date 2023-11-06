from modelo.paciente import Paciente
from modelo.examen import Examen
from modelo.tipoExamen import TipoExamen
from modelo.contacto import Contacto
from modelo.apoderado import Apoderado

from datetime import datetime


def main():
    nombre_archivo = 'inputs/lab_input.txt'
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    examenes = []
    for linea in lineas:
        partes = linea.strip().split('|')
        if len(partes) == 1:
            fecha_actual = parsear_fecha(partes[0])
        elif len(partes) == 10:
            hora_examen, nombre_examen, horario_especial_examen, nombre_paciente, rango_edad_paciente, tipo_identificacion_paciente, identificacion_paciente, telefono_contacto, fecha_nacimiento_paciente, _ = partes
            correo_contacto = "dummy@hotmail.com"
            contacto = Contacto(telefono_contacto, correo_contacto)
            paciente = Paciente(nombre_paciente, parsear_fecha(fecha_nacimiento_paciente), tipo_identificacion_paciente, identificacion_paciente, contacto)
            tipoExamen = TipoExamen(nombre_examen, horario_especial_examen)
            fecha_hora_examen = combinar_fecha_hora(fecha_actual, hora_examen)
            examen = Examen(paciente, tipoExamen, fecha_hora_examen)
            examenes.append(examen)
        elif len(partes) == 15:
            # Con Apoderado
            hora_examen, nombre_examen, horario_especial_examen, nombre_paciente, rango_edad_paciente, tipo_identificacion_paciente, identificacion_paciente, telefono_contacto, fecha_nacimiento_paciente, es_apoderado, nombre_apoderado, tipo_identificacion_apoderado, identificacion_apoderado, fecha_nacimiento_apoderado, _ = partes
            correo_contacto = "dummy@hotmail.com"
            contacto = Contacto(telefono_contacto, correo_contacto)
            apoderado = Apoderado(nombre_apoderado, parsear_fecha(fecha_nacimiento_apoderado), tipo_identificacion_apoderado, identificacion_apoderado)
            paciente = Paciente(nombre_paciente, parsear_fecha(fecha_nacimiento_paciente), tipo_identificacion_paciente, identificacion_paciente, contacto, apoderado)
            tipoExamen = TipoExamen(nombre_examen, horario_especial_examen)
            fecha_hora_examen = combinar_fecha_hora(fecha_actual, hora_examen)
            examen = Examen(paciente, tipoExamen, fecha_hora_examen)
            examenes.append(examen)
        elif len(partes) == 11:
            # Nuevo Examen Sin Apoderado
            dia_examen, hora_examen, nombre_examen, horario_especial_examen, nombre_paciente, rango_edad_paciente, tipo_identificacion_paciente, identificacion_paciente, telefono_contacto, fecha_nacimiento_paciente, _ = partes
            correo_contacto = "dummy@hotmail.com"
            contacto = Contacto(telefono_contacto, correo_contacto)
            paciente = Paciente(nombre_paciente, parsear_fecha(fecha_nacimiento_paciente), tipo_identificacion_paciente, identificacion_paciente, contacto)
            tipoExamen = TipoExamen(nombre_examen, horario_especial_examen)
            fecha_hora_examen = combinar_fecha_hora(parsear_fecha(dia_examen), hora_examen)
            examen = Examen(paciente, tipoExamen, fecha_hora_examen)
            examenes.append(examen)
        elif len(partes) == 16:
            # Nuevo Examen Con Apoderado
            dia_examen, hora_examen, nombre_examen, horario_especial_examen, nombre_paciente, rango_edad_paciente, tipo_identificacion_paciente, identificacion_paciente, telefono_contacto, fecha_nacimiento_paciente, es_apoderado, nombre_apoderado, tipo_identificacion_apoderado, identificacion_apoderado, fecha_nacimiento_apoderado, _ = partes
            correo_contacto = "dummy@hotmail.com"
            contacto = Contacto(telefono_contacto, correo_contacto)
            apoderado = Apoderado(nombre_apoderado, parsear_fecha(fecha_nacimiento_apoderado), tipo_identificacion_apoderado, identificacion_apoderado)
            paciente = Paciente(nombre_paciente, parsear_fecha(fecha_nacimiento_paciente), tipo_identificacion_paciente, identificacion_paciente, contacto, apoderado)
            tipoExamen = TipoExamen(nombre_examen, horario_especial_examen)
            fecha_hora_examen = combinar_fecha_hora(parsear_fecha(dia_examen), hora_examen)
            examen = Examen(paciente, tipoExamen, fecha_hora_examen)
            examenes.append(examen)  

    print("-------------------------------------------------------")
    imprimir_listado_examenes(examenes)

def parsear_fecha(textoFecha):
    try:
        fecha = datetime.strptime(textoFecha, '%Y-%m-%d')
        return fecha
    except ValueError:
        return None



def combinar_fecha_hora(fecha, hora_string):
    try:
        hora = datetime.strptime(hora_string, '%H:%M')
        fecha_hora_combinada = datetime(year=fecha.year, month=fecha.month, day=fecha.day, hour=hora.hour, minute=hora.minute)
        return fecha_hora_combinada
    except ValueError:
        return None

def obtener_fechas_examenes(examenes):
    examenes_por_fecha = {}
    for examen in examenes:
        fecha = examen.fecha_hora_examen.date()
        if fecha not in examenes_por_fecha:
            examenes_por_fecha[fecha] = []
        examenes_por_fecha[fecha].append(examen)
    
    return examenes_por_fecha

def imprimir_listado_examenes(examenes):
    examenes_por_fecha = obtener_fechas_examenes(examenes)
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