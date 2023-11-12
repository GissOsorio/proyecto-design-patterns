from modelo.examenState import ExamenState

class ExamenNuevoState(ExamenState):
    def realizar_examen(self):
        if self.contexto.es_fecha_futura(self.contexto.examen.fecha_hora_examen):
            print("Guardando examen...")
            self.contexto.cambiar_estado("guardado")
        else:
            raise ValueError("No se puede crear una cita en una fecha pasada")