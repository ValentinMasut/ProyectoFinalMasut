from persona import Persona

class Alumno(Persona):
    def __init__(self, nombre, dni, email):
        super().__init__(nombre, dni, email)
        self.notas = {
            "tp": [],
            "parcial": [],
            "final": []
        }
    #Mostrar datos del alumno
    def mostrarInfo(self):
        return f"Nombre: {super().mostrarInfo()} - Notas: {self.notas}"
    
    #Agregar notas a un alumno en especifico
    def cargarNotas(self,tipo,nota):
       while True: 
        if tipo.lower() in self.notas:
            self.notas[tipo.lower()].append(nota)
            break
        else:
            print(f"Tipo de nota {tipo}, no es valido, ingrese otro (Los correctos son parcial,final,tp): ")
            tipo = input()
    #Mostrar que notas aprobo de cada tipo un alumno elegido (Estos son los que sacaron mas de 6 en la nota especificada)
    def mostrarNotaAprobadaPorTipo(self,tipo):
        if tipo in self.notas:
            notasFiltradas = list(filter(lambda n:n>=6, self.notas[tipo]))
            print(f"Notas de tipo: {tipo} aprobadas de {self.nombre}: {notasFiltradas}")

    #Se utiliza para poder imprimir el objeto en pantalla de esta manera a la hora de utilizarlo
    def __str__(self):
        return f"Nombre: {self.nombre} - DNI: {self.dni} - Email: {self.email}"
    
    #Saca un promedio de todas las notas del alumno incluyendo tanto parciales como tp y finales.
    def promNotaTotal(self):
        prom = sum(sum(list) for list in self.notas.values())/sum(len(list) for list in self.notas.values())
        return prom
    
    #Calcula el promedio de un tipo de nota especifico
    def promPorTipo(self,tipo):
        if tipo in self.notas:
            prom = sum(self.notas[tipo])/(len(self.notas.values())-1)
            return prom
        else:
            return "El tipo no es correcto"