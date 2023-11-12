from modelo.horarioAtencionLaboratorio import HorarioAtencionLaboratorio
from datetime import datetime
import unittest

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

if __name__ == '__main__':
    unittest.main()