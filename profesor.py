from persona import Persona
class Profesor(Persona):
    def __init__(self, nombre, dni, email,cargo):
        super().__init__(nombre, dni, email)
        self.cursos = []
        self.cargo = cargo
    
    #Imprime los datos del profesor
    def mostrarInfo(self):
        return f"{super().mostrarInfo()} - Cursos a cargo: {self.cursos}, Puesto: {self.cargo}"
    
    def asignarCursos(self,curso):
        return self.cursos.append(curso)
    
    #Se usa para poder mostrar por pantalla de esta manera al objeto profesor de esta manera especifica para cuando se llama por otra clase
    def __str__(self):
        return f"Nombre: {self.nombre} - DNI: {self.dni} - Email: {self.email} - Puesto: {self.cargo}"
    
    
    