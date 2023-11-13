from modelo.persona import Persona
from modelo.paciente import Paciente
from datetime import datetime
import unittest

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
    

if __name__ == '__main__':
    unittest.main()