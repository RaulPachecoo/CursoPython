#EJERCICIO 3
'''
Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; 
luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. 
Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. 
Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno
'''

class Fabrica():
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio

    
class Moto(Fabrica):
    def datos(self):
        print("La cantidad de llantas es de:", self._llantas)
        print("El color de la moto es:", self._color)
        print("El precio de la moto es de:", self._precio)

class Coche(Fabrica):
    def datos(self):
        print("La cantidad de llantas es de:", self._llantas)
        print("El color del coche es:", self._color)
        print("El precio del coche es de:", self._precio)
        

moto = Moto(2, "Negro", 5000)
moto.datos()
coche = Coche(4, "Blanco", 30000)
coche.datos()