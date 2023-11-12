from modelo.examenState import ExamenState

class ExamenGuardadoState(ExamenState):
    def realizar_examen(self):
        print("El examen ya ha sido guardado.")