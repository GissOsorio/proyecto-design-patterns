from modelo.paciente import Paciente
from modelo.examen import Examen
from modelo.tipoExamen import TipoExamen
from modelo.contacto import Contacto
from modelo.apoderado import Apoderado
from modelo.fecha import Fecha

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
            contacto = obtener_contacto(partes) 
            paciente = obtener_paciente(partes, contacto)
            tipoExamen = obtener_tipo_examen(partes)
            fecha_hora_examen = revisar_fecha(partes, fecha_actual)
            try:
                fecha = Fecha(fecha_hora_examen)
                examen = agregar_examen(paciente, tipoExamen, fecha.fecha_hora_examen, "guardado")
                examenes.append(examen)
            except ValueError as e:
                print("Error:", e)
        elif len(partes) == 15:
            # Con Apoderado
            contacto = obtener_contacto_con_apoderado(partes) 
            apoderado = obtener_apoderado(partes)
            paciente = obtener_paciente_con_apoderado(partes, contacto, apoderado)
            tipoExamen = obtener_tipo_examen_con_apoderado(partes)
            fecha_hora_examen = revisar_fecha_con_apoderado(partes, fecha_actual)
            try:
                fecha = Fecha(fecha_hora_examen)
                examen = agregar_examen(paciente, tipoExamen, fecha.fecha_hora_examen, "guardado")
                examenes.append(examen)
            except ValueError as e:
                print("Error:", e)
        elif len(partes) == 11:
            # Nuevo Examen Sin Apoderado
            contacto = guardar_contacto(partes) 
            paciente = guardar_paciente(partes, contacto)
            tipoExamen = guardar_tipo_examen(partes)
            fecha_hora_examen = guardar_fecha(partes)
            try:
                fecha = Fecha(fecha_hora_examen)
                examen = agregar_examen(paciente, tipoExamen, fecha.fecha_hora_examen, "nuevo")
                examenes.append(examen)
            except ValueError as e:
                print("Error:", e)
        elif len(partes) == 16:
            # Nuevo Examen Con Apoderado
            contacto = guardar_contacto_con_apoderado(partes) 
            apoderado = guardar_apoderado(partes)
            paciente = guardar_paciente_con_apoderado(partes, contacto, apoderado)
            tipoExamen = guardar_tipo_examen_con_apoderado(partes)
            fecha_hora_examen = guardar_fecha_con_apoderado(partes)
            try:
                fecha = Fecha(fecha_hora_examen)
                examen = agregar_examen(paciente, tipoExamen, fecha.fecha_hora_examen, "guardado")
                examenes.append(examen)
            except ValueError as e:
                print("Error:", e)

    print("-------------------------------------------------------")
    imprimir_listado_examenes(examenes)

def validar_citas_simultaneas(fecha_hora, examenes):
    contador = 0
    for examen in examenes:
        print(examen.fecha_hora_examen)
        if fecha_hora.date() == examen.fecha_hora_examen.date() and fecha_hora.time() == examen.fecha_hora_examen.time():
            contador += 1
            
    if contador >= 2:
        return False
    
    return True

def obtener_apoderado(partes):
    _, _, _, _, _, _, _, _, _, _, nombre_apoderado, tipo_identificacion_apoderado, identificacion_apoderado, fecha_nacimiento_apoderado, _ = partes
    apoderado = Apoderado(nombre_apoderado, parsear_fecha(fecha_nacimiento_apoderado), tipo_identificacion_apoderado, identificacion_apoderado)
    return apoderado

def obtener_paciente_con_apoderado(partes, contacto, apoderado):
    _, _, _, nombre_paciente, rango_edad_paciente, tipo_identificacion_paciente, identificacion_paciente, _, fecha_nacimiento_paciente, _, _ ,_ ,_ ,_, _ = partes
    paciente = Paciente(nombre_paciente, parsear_fecha(fecha_nacimiento_paciente), tipo_identificacion_paciente, identificacion_paciente, contacto, apoderado)
    return paciente

def obtener_contacto_con_apoderado(partes):
    _, _, _, _, _, _, _, telefono_contacto, _, _, _, _, _, _, _ = partes
    correo_contacto = "dummy@hotmail.com"
    contacto = Contacto(telefono_contacto, correo_contacto)
    return contacto

def obtener_tipo_examen_con_apoderado(partes):
    _, nombre_examen, horario_especial_examen, _, _, _, _, _, _, _, _, _, _, _, _ = partes
    tipoExamen = TipoExamen(nombre_examen, horario_especial_examen)
    return tipoExamen

def revisar_fecha_con_apoderado(partes, fecha_actual):
    hora_examen, _, _, _, _, _, _, _, _, _, _, _, _, _, _ = partes
    fecha_hora_examen = combinar_fecha_hora(fecha_actual, hora_examen)
    return fecha_hora_examen

def guardar_apoderado(partes):
    _, _, _, _, _, _, _, _, _, _, _, nombre_apoderado, tipo_identificacion_apoderado, identificacion_apoderado, fecha_nacimiento_apoderado, _ = partes
    apoderado = Apoderado(nombre_apoderado, parsear_fecha(fecha_nacimiento_apoderado), tipo_identificacion_apoderado, identificacion_apoderado)
    return apoderado

def guardar_paciente_con_apoderado(partes, contacto, apoderado):
    _, _, _, _, nombre_paciente, rango_edad_paciente, tipo_identificacion_paciente, identificacion_paciente, _, fecha_nacimiento_paciente, _, _ ,_ ,_ ,_, _ = partes
    paciente = Paciente(nombre_paciente, parsear_fecha(fecha_nacimiento_paciente), tipo_identificacion_paciente, identificacion_paciente, contacto, apoderado)
    return paciente

def guardar_contacto_con_apoderado(partes):
    _, _, _, _, _, _, _, _, telefono_contacto, _, _, _, _, _, _, _ = partes
    correo_contacto = "dummy@hotmail.com"
    contacto = Contacto(telefono_contacto, correo_contacto)
    return contacto

def guardar_tipo_examen_con_apoderado(partes):
    _, _, nombre_examen, horario_especial_examen, _, _, _, _, _, _, _, _, _, _, _, _ = partes
    tipoExamen = TipoExamen(nombre_examen, horario_especial_examen)
    return tipoExamen

def guardar_fecha_con_apoderado(partes):
    fecha_examen, hora_examen, _, _, _, _, _, _, _, _, _, _, _, _, _, _ = partes
    fecha_hora_examen = combinar_fecha_hora(parsear_fecha(fecha_examen),hora_examen)

    return fecha_hora_examen

def guardar_contacto(partes):
    _, _, _, _, _, _, _, _, telefono_contacto, _, _ = partes
    correo_contacto = "dummy@hotmail.com"
    contacto = Contacto(telefono_contacto, correo_contacto)
    return contacto

def obtener_contacto(partes):
    _, _, _, _, _, _, _, telefono_contacto, _, _ = partes
    correo_contacto = "dummy@hotmail.com"
    contacto = Contacto(telefono_contacto, correo_contacto)
    return contacto

def obtener_paciente(partes, contacto):
    _, _, _, nombre_paciente, rango_edad_paciente, tipo_identificacion_paciente, identificacion_paciente, _, fecha_nacimiento_paciente, _ = partes
    paciente = Paciente(nombre_paciente, parsear_fecha(fecha_nacimiento_paciente), tipo_identificacion_paciente, identificacion_paciente, contacto)
    return paciente

def obtener_tipo_examen(partes):
    _, nombre_examen, horario_especial_examen, _, _, _, _, _, _, _ = partes
    tipoExamen = TipoExamen(nombre_examen, horario_especial_examen)
    return tipoExamen

def revisar_fecha(partes, fecha_actual):
    hora_examen, _, _, _, _, _, _, _, _, _ = partes
    fecha_hora_examen = combinar_fecha_hora(fecha_actual, hora_examen)
    return fecha_hora_examen

def guardar_contacto(partes):
    _, _, _, _, _, _, _, _, telefono_contacto, _, _ = partes
    correo_contacto = "dummy@hotmail.com"
    contacto = Contacto(telefono_contacto, correo_contacto)
    return contacto

def guardar_paciente(partes, contacto):
    _, _, _, _, nombre_paciente, rango_edad_paciente, tipo_identificacion_paciente, identificacion_paciente, _, fecha_nacimiento_paciente, _ = partes
    paciente = Paciente(nombre_paciente, parsear_fecha(fecha_nacimiento_paciente), tipo_identificacion_paciente, identificacion_paciente, contacto)
    return paciente

def guardar_tipo_examen(partes):
    _, _, nombre_examen, horario_especial_examen, _, _, _, _, _, _, _ = partes
    tipoExamen = TipoExamen(nombre_examen, horario_especial_examen)
    return tipoExamen

def guardar_fecha(partes):
    fecha_examen, hora_examen, _, _, _, _, _, _, _, _, _ = partes
    fecha_hora_examen = combinar_fecha_hora(parsear_fecha(fecha_examen), hora_examen)
    return fecha_hora_examen

def agregar_examen(paciente, tipoExamen, fecha_hora_examen, estado):
    examen = Examen(paciente, tipoExamen, fecha_hora_examen, estado)
    return examen

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