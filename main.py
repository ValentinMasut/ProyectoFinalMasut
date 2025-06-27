from alumno import Alumno
from profesor import Profesor
from curso import Curso

#Instanciar profesores
docente1 = Profesor("David Sanchez",21125987, "Dsanchez323@gmail.com","Docente")
docente1.asignarCursos("Programacion")
docente2 = Profesor("Facundo Zarate",32514456,"Facuzarate@gmail.com","Regente")
docente2.asignarCursos("Programacion")

#Instanciar alumnos
alumno1 = Alumno("Jose Carlos",42126123,"josesito@gmail")
alumno2 = Alumno("Pablob",41345623,"judio@gmail")
alumno3 = Alumno("Valentin",623,"goku@gmail")

#Instanciar los cursos y asignarles sus docentes y alumnos
curso1 = Curso("Programacion",123)
curso1.asigDoncente(docente1)
curso1.asigDoncente(docente2)
curso1.addEstudiantes(alumno1)
curso1.addEstudiantes(alumno2)
curso1.addEstudiantes(alumno3)

#Cargarles notas a los alumnos
alumno1.cargarNotas("parcial", 9)
alumno1.cargarNotas("TP", 6)
alumno1.cargarNotas("tp",7)
alumno1.cargarNotas("final",5)
alumno2.cargarNotas("final",6)
alumno3.cargarNotas("FINAL", 8)
#Nota mal cargada a proposito, el tipo no es correcto, si se habilita entra en bucle hasta que se ingrese un tipo correcto
#alumno1.cargarNotas("hola", 10)
print("--------------------------------------------------------------")
#Muestra la informacion del curso incluyendo listado de alumnos y los profesores a cargo
print(f"Curso: {curso1.nombre} - Codigo de curso: {curso1.codigo}")
print("Profesor/es a cargo: ")
curso1.mostrarProfesor()
print("--------------------------------------------------------------")
print("Listado de alumnos del curso: ")
curso1.listarAlumnos()
#Listado de alumnos aprobados (Esto filtra en base a que todos las notas del apartado final sean 6 o mas)
print("--------------------------------------------------------------")
print("Los alumnos aprobados en este  curso son: ")
aprobados = curso1.alumnosAprobados()
for alumno in aprobados:
    print(alumno)
print("--------------------------------------------------------------")
#Mostrar nota maxima y minima de un curso especifico
print(curso1.notaMaxima())
print(curso1.notaMinima())
print("--------------------------------------------------------------")
#Mostrar info de un alumno en especifico
print(alumno1.mostrarInfo())
print("--------------------------------------------------------------")
#Mostrar datos de un docente en especifico
print(docente1.mostrarInfo())
print("--------------------------------------------------------------")
#Calculos con notas de alumnos
print(alumno1.promNotaTotal())
alumno1.mostrarNotaAprobadaPorTipo("tp")
print(alumno1.promPorTipo("tp"))
print("--------------------------------------------------------------")



