class TipoExamen:
    def __init__(self, nombre, horario):
        if not nombre:
            raise ValueError("Faltan datos del Tipo del Examen.")

        self.nombre = nombre
        self.horario = horario

    def tipoExamen(self):
        return f"TipoExamen: {self.nombre}, {self.horario}"
