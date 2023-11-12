from modelo.examenNuevoState import ExamenNuevoState
from modelo.examenGuardadoState import ExamenGuardadoState

class ExamenContexto:
    def __init__(self, examen):
        self.examen = examen
        self.estado = ExamenNuevoState(self)

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado == "nuevo":
            self.estado = ExamenNuevoState(self)
        elif nuevo_estado == "guardado":
            self.estado = ExamenGuardadoState(self)
        else:
            raise ValueError("Estado no válido.")

    def es_fecha_futura(self, fecha):
        return self.examen.es_fecha_futura(fecha)

    def es_hora_especial(self, fecha_hora):
        return self.examen.es_hora_especial(fecha_hora)