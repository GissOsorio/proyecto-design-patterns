class TipoExamen:
    def __init__(self, nombre, es_horario_especial):
        self.nombre = nombre
        self.es_horario_especial = es_horario_especial

    def tipoExamen(self):
        return f"TipoExamen: {self.nombre}, {self.es_horario_especial}"
