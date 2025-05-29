#EJERCICIO 5
'''
Crear un programa con tres clases Universidad, con atributos nombre 
(Donde se almacena el nombre de la Universidad). Otra llamada Carerra, 
con los atributos especialidad (En donde me guarda la especialidad de un estudiante). 
Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. 
El programa debe imprimir la especialidad, edad, nombre y universidad de 
dicho estudiante con un objeto llamado persona.
'''

class Universidad():
    def __init__(self, nombreUniversidad):
        self._nombreUniversidad = nombreUniversidad
    
class Carrera():
    def carrera(self, especialidad):
        self._especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def datos(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        print("Nombre: {} \nEdad: {} \nUniversidad: {} \nCarrera: {}".format(self._nombre, self._edad, self._nombreUniversidad, self._especialidad))

estudiante = Estudiante("UGR")
estudiante.carrera("Informática")
estudiante.datos("Raúl", 20)