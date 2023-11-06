from modelo.paciente import Paciente
from modelo.examen import Examen
from modelo.tipoExamen import TipoExamen
from datetime import datetime


def main():
    examenes = []
    nombre_archivo = 'inputs/lab_input.txt'
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        partes = linea.strip().split('|')
        print(len(partes))
        if len(partes) == 1:
            fecha_actual = parsearFecha(partes[0])
        elif len(partes) == 10:
            hora_string, nombre, tipo, pacienteNombre, edad, tipoIdentificacion, identificacion, celular, fechaNacimiento, _ = partes
            paciente = Paciente(pacienteNombre, parsearFecha(fechaNacimiento), tipoIdentificacion, identificacion)
            print(paciente.paciente())
            print(f"Edad: {paciente.esMayorDeEdad()}")   
            tipoExamen = TipoExamen(nombre, esHorarioEspecial(tipo))
            fechaHoraExamen = combinarFechaHora(fecha_actual, hora_string)
            examen = Examen(paciente, tipoExamen, fechaHoraExamen)
            examenes.append(examen)
            print(examen.examen())

    # print(contenido)
    # fecha_nacimiento = datetime(1990, 5, 15) 
    # paciente = Paciente("Juan Pérez", fecha_nacimiento, "C", "123456789")
    # print(paciente.paciente())
    # print(f"Edad: {paciente.esMayorDeEdad()}")
    # tipoExamen = TipoExamen("GLUCOSA", True)
    # fechaHoraExamen = datetime(2023, 11, 5, 15, 30, 0)
    # examen = Examen(paciente, tipoExamen, fechaHoraExamen)
    # print(examen.examen())


def parsearFecha(textoFecha):
    try:
        fecha = datetime.strptime(textoFecha, '%Y-%m-%d')
        return fecha
    except ValueError:
        return None

def esHorarioEspecial(tipo):
    if "EARLY" in tipo:
        return True
    else:
        return False

def combinarFechaHora(fecha, hora_string):
    try:
        hora = datetime.strptime(hora_string, '%H:%M')
        fecha_hora_combinada = datetime(year=fecha.year, month=fecha.month, day=fecha.day, hour=hora.hour, minute=hora.minute)
        return fecha_hora_combinada
    except ValueError:
        return None

if __name__ == "__main__":
    main()