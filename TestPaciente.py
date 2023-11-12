from modelo.persona import Persona
from modelo.paciente import Paciente
import unittest

class TestPaciente(unittest.TestCase):  

    def test_tiene_apoderado(self):  
        
        persona = Persona
        persona.apoderado = Persona
        persona.es_mayor_de_edad

        paciente = Paciente
        tiene_apoderado = paciente.tiene_apoderado(persona)
        self.assertEqual(tiene_apoderado, True)           
    

if __name__ == '__main__':
    unittest.main()