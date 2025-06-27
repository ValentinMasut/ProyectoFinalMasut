class Persona:
    def __init__(self,nombre,dni,email):
        self.nombre = nombre
        self.dni = dni
        self.email = email
    #Mostrar datos persona
    def mostrarInfo(self):
        return f"{self.nombre} - DNI: {self.dni} - Email: {self.email}"
