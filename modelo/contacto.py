from datetime import datetime

class Contacto:
    def __init__(self, telefono, correo):
        self.telefono = telefono
        self.correo = correo

    def contacto(self):
        return f"Contacto: {self.telefono}, {self.correo}"

