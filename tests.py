from modelo.examen import Examen
from modelo.persona import Persona
from modelo.horarioAtencionLaboratorio import HorarioAtencionLaboratorio
from modelo.paciente import Paciente
from main import validar_cita_paciente
from main import validar_citas_simultaneas
from datetime import datetime
import unittest

class TestExamen(unittest.TestCase):  
    HORARIO_APERTURA_EARLY = "7:00"
    HORARIO_CIERRE_EARLY = "9:00"
    FECHA_HORA_EXAMEN = datetime(2023, 11, 10, 8, 0)

    def test_es_hora_especial(self):  
        examen = Examen
        examen.horario_apertura = self.HORARIO_APERTURA_EARLY
        examen.horario_cierre = self.HORARIO_CIERRE_EARLY

        es_hora_especial = examen.es_hora_especial(examen, self.FECHA_HORA_EXAMEN)
        self.assertEqual(es_hora_especial, True)           

    def test_es_fecha_futura(self):  
        examen = Examen
        examen.horario_apertura = self.HORARIO_APERTURA_EARLY
        examen.horario_cierre = self.HORARIO_CIERRE_EARLY

        es_fecha_futura = examen.es_fecha_futura(examen, self.FECHA_HORA_EXAMEN)
        self.assertEqual(es_fecha_futura, False)   

class TestHorarioAtencionLaboratorio(unittest.TestCase):  
    DIAS_ATENCION = [0,1,2,3,4]
    HORARIO_APERTURA = datetime.strptime("7:00", "%H:%M").time()
    HORARIO_CIERRE = datetime.strptime("16:00", "%H:%M").time()
    FERIADOS = {"08-10", "11-03"} 
    FECHA_HORA_EXAMEN = datetime(2023, 11, 10, 9, 0)

    def test_es_dia_laborable(self):  
        horario_atencion_laboratorio = HorarioAtencionLaboratorio

        horario_atencion_laboratorio.dias_semana = self.DIAS_ATENCION
        esDiaLaborable = horario_atencion_laboratorio.es_dia_laborable(horario_atencion_laboratorio, self.FECHA_HORA_EXAMEN)
        self.assertEqual(esDiaLaborable, True)           

    def test_es_hora_laborable(self):  
        horario_atencion_laboratorio = HorarioAtencionLaboratorio
        
        horario_atencion_laboratorio.horario_apertura = self.HORARIO_APERTURA
        horario_atencion_laboratorio.horario_cierre = self.HORARIO_CIERRE
        esHoraLaborable = horario_atencion_laboratorio.es_hora_laborable(horario_atencion_laboratorio, self.FECHA_HORA_EXAMEN)
        self.assertEqual(esHoraLaborable, True)   

    def test_es_feriado(self):  
        horario_atencion_laboratorio = HorarioAtencionLaboratorio
        
        horario_atencion_laboratorio.dias_feriados = self.FERIADOS
        esFeriado = horario_atencion_laboratorio.es_feriado(horario_atencion_laboratorio, self.FECHA_HORA_EXAMEN)
        self.assertEqual(esFeriado, False)   

    def test_es_intervalo_de_cita_valido(self):  
        horario_atencion_laboratorio = HorarioAtencionLaboratorio
        
        esIntervaloValido = horario_atencion_laboratorio.es_intervalo_de_cita_valido(horario_atencion_laboratorio, self.FECHA_HORA_EXAMEN)
        self.assertEqual(esIntervaloValido, True)   

class TestPersona(unittest.TestCase):  

    def test_es_mayor_de_edad(self):  
        
        persona = Persona
        persona.fecha_nacimiento = datetime(1988, 11, 10, 9, 0)
        es_mayor_de_edad = persona.es_mayor_de_edad(persona)
        self.assertEqual(es_mayor_de_edad, True)         

    def test_tiene_apoderado(self):  
        
        persona = Persona
        persona.apoderado = Persona

        paciente = Paciente
        tiene_apoderado = paciente.tiene_apoderado(persona)
        self.assertEqual(tiene_apoderado, True)   

class TestMain(unittest.TestCase):  
    DIAS_ATENCION = [0,1,2,3,4]
    HORARIO_APERTURA = datetime.strptime("7:00", "%H:%M").time()
    HORARIO_CIERRE = datetime.strptime("16:00", "%H:%M").time()
    FERIADOS = {"08-10", "11-03"} 
    FECHA_HORA_EXAMEN = datetime(2023, 11, 10, 9, 0)

    def test_validar_cita_paciente(self):  
        paciente = Paciente
        paciente.identificacion = "1721872073"

        examen = Examen
        examen.paciente = Paciente
        examen.paciente.identificacion = "1721872073"
        examen.fecha_hora_examen = datetime(2023, 11, 10, 9, 0)

        examenes = []
        examenes.append(examen)

        with self.assertRaises(ValueError) as contexto:
            validar_cita_paciente(paciente, self.FECHA_HORA_EXAMEN, examenes)
        self.assertEqual(str(contexto.exception), "El paciente ya tiene una cita en el mismo horario.")

    def test_validar_citas_simultaneas(self):  
        
        examen1 = Examen
        examen1.fecha_hora_examen = datetime(2023, 11, 10, 9, 0)
        examen2 = Examen
        examen2.fecha_hora_examen = datetime(2023, 11, 10, 9, 0)
        
        examenes = []
        examenes.append(examen1)
        examenes.append(examen2)

        with self.assertRaises(ValueError) as contexto:
            validar_citas_simultaneas(self.FECHA_HORA_EXAMEN, examenes)
        self.assertEqual(str(contexto.exception), "Se pueden hacer hasta 2 reservas en el mismo horario")

if __name__ == '__main__':
    unittest.main()