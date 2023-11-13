from modelo.examen import Examen
from  modelo.paciente import Paciente
from main import validar_cita_paciente
from main import validar_citas_simultaneas
from datetime import datetime
import unittest

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