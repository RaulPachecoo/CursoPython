#EJERCICIO 1
'''
Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre 
y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar 
un mensaje con el resultado de la nota y si ha aprobado o no.
'''

class Estudiante():
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    def __str__(self):
        return "Nombre: {} \nNota: {}".format(self._nombre, self._nota)
    
    def resultadoNota(self):
        if self._nota >=5 and self._nota <= 10:
            print("El estudiante {} a aprobado. ¡ENHORABUENA!".format(self._nombre))
        else:
            print("El estudiante {} a suspendido :(".format(self._nombre))


estudiante = Estudiante("Raúl", 9)

print(estudiante)

estudiante.resultadoNota()

