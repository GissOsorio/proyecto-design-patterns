class TipoExamen:
    def __init__(self, nombre, horario):
        self.nombre = nombre
        self.horario = horario

    def tipoExamen(self):
        return f"TipoExamen: {self.nombre}, {self.horario}"
