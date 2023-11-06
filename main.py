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
            hora_string, nombre, tipo, paciente_nombre, edad, tipo_identificacion, identificacion, telefono, fecha_nacimiento, _ = partes
            correo = "dummy@hotmail.com"
            contacto = Contacto(telefono, correo)
            paciente = Paciente(paciente_nombre, parsear_fecha(fecha_nacimiento), tipo_identificacion, identificacion, contacto)
            print(paciente.paciente())
            print(f"Edad: {paciente.es_mayor_de_edad()}")   
            tipoExamen = TipoExamen(nombre, es_horario_especial(tipo))
            fecha_hora_examen = combinar_fecha_hora(fecha_actual, hora_string)
            examen = Examen(paciente, tipoExamen, fecha_hora_examen)
            examenes.append(examen)
            print(examen.examen())
        elif len(partes) == 15:
            # Con Apoderado
            hora_string, nombre, tipo, paciente_nombre, edad, tipo_identificacion, identificacion, telefono, fecha_nacimiento, es_apoderado, apoderado_nombre, apoderado_tipo_identificacion, apoderado_identificacion, apoderado_fecha_nacimiento, _ = partes
            correo = "dummy@hotmail.com"
            contacto = Contacto(telefono, correo)
            apoderado = Apoderado(apoderado_nombre, parsear_fecha(apoderado_fecha_nacimiento), apoderado_tipo_identificacion, apoderado_identificacion)
            paciente = Paciente(paciente_nombre, parsear_fecha(fecha_nacimiento), tipo_identificacion, identificacion, contacto, apoderado)
            print(paciente.apoderado.nombre)
            print(f"Edad: {paciente.es_mayor_de_edad()}")   
            tipoExamen = TipoExamen(nombre, es_horario_especial(tipo))
            fecha_hora_examen = combinar_fecha_hora(fecha_actual, hora_string)
            examen = Examen(paciente, tipoExamen, fecha_hora_examen)
            examenes.append(examen)
            print(examen.examen())
        elif len(partes) == 11:
            print(len(partes))
            # Nuevo Examen
        elif len(partes) == 16:
            print(len(partes))
            # Nuevo Examen Con Apoderado   

def parsear_fecha(textoFecha):
    try:
        fecha = datetime.strptime(textoFecha, '%Y-%m-%d')
        return fecha
    except ValueError:
        return None

def es_horario_especial(tipo):
    if "EARLY" in tipo:
        return True
    else:
        return False

def combinar_fecha_hora(fecha, hora_string):
    try:
        hora = datetime.strptime(hora_string, '%H:%M')
        fecha_hora_combinada = datetime(year=fecha.year, month=fecha.month, day=fecha.day, hour=hora.hour, minute=hora.minute)
        return fecha_hora_combinada
    except ValueError:
        return None

if __name__ == "__main__":
    main()