from modelo.fecha import Fecha
from datetime import datetime

import unittest

class FechaTest(unittest.TestCase):
    
    def test_es_dia_laborable(self):
        with self.assertRaises(ValueError) as contexto:
            fecha = datetime(2024, 1, 6, 7, 0)
            fecha = Fecha(fecha)
        self.assertEqual(str(contexto.exception), "El establecimiento solo opera de lunes a viernes from FECHA.")

    def test_es_dia_laborable(self):
        with self.assertRaises(ValueError) as contexto:
            fecha = datetime(2023, 1, 5, 6, 0)
            fecha = Fecha(fecha)
        self.assertEqual(str(contexto.exception), "El establecimiento solo opera de 7:00 a 16:00.")

if __name__ == '__main__':
    unittest.main()