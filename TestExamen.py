from modelo.examen import Examen
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

if __name__ == '__main__':
    unittest.main()