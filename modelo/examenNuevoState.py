from modelo.examenState import ExamenState

class ExamenNuevoState(ExamenState):
    def realizar_examen(self):
        if self.contexto.es_fecha_futura(self.contexto.fecha_hora_examen):
            print("Realizando examen...")
            self.contexto.cambiar_estado("realizado")
        else:
            print("No se puede realizar el examen en una fecha pasada.")