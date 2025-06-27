from profesor import Profesor
from alumno import Alumno
from persona import Persona
class Curso:
    def __init__(self, nombre, codigo):
        self.estudiantes = []
        self.codigo = codigo
        self.nombre = nombre
        self.profesor = []
    
    #Asignar estudiante/es al curso
    def addEstudiantes(self, estudiante):
        self.estudiantes.append(estudiante)
    
    #Asigrnar docente/es al curso
    def asigDoncente(self,docente):
        self.profesor.append(docente)

    #Lista de todos los alumnos del curso
    def listarAlumnos(self):
        for alumno in self.estudiantes:
            print(alumno)

    #Mostrar datos de los profesores del curso
    def mostrarProfesor(self):
        for profesor in self.profesor:
            print(profesor)

    #Esta funcion crea una lista con los alumnos aprobados en el curso (para aprobar todas las notas de la categoria final deben ser 6 o mas)
    def alumnosAprobados(self):
        return list(filter(lambda x: all(nota >=6 for nota in x.notas.get("final",[])),self.estudiantes))
    
    #Funcion para filtrar la nota mas alta (categoria final)
    def notaMaxima(self):
        if not self.estudiantes:
            return "No hay alumnos cargados"
        else:
            alumno = max(self.estudiantes, key= lambda x: max(x.notas.get("final",[0])))
            notaMax = max(alumno.notas.get("final",[0]))
            return f"El alumno con mayor nota es: {alumno.nombre} con una nota de: {notaMax}"
    
    #Funcion para filtrar la nota mas baja (categoria final)
    def notaMinima(self):
        if not self.estudiantes:
            return "No hay alumnos cargados"
        else:
            alumno = min(self.estudiantes, key= lambda x: min(x.notas.get("final",[0])))
            notaMin = min(alumno.notas.get("final",[0]))
            return f"El alumno con la menor nota es: {alumno.nombre} con una nota de: {notaMin}"
        