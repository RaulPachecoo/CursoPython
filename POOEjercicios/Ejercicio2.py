#EJERCICIO 2
'''
Realizar un programa en el cual se declaren dos valores enteros por teclado 
utilizando el método __init__. Calcular después la suma, resta, multiplicación 
y división. Utilizar un método para cada una e imprimir los resultados obtenidos. 
Llamar a la clase Calculadora.
'''

class Calculadora():
    def __init__(self):
        self._num1 = int(input("Introduce el primer valor: "))
        self._num2 = int(input("Introduce el segundo valor: "))

    def suma(self):
        return self._num1 + self._num2
    
    def resta(self):
        return self._num1 - self._num2
    
    def multiplicacion(self):
        return self._num1 * self._num2
    
    def division(self):
        if self._num2 == 0:
            return "No se puede dividir por cero"
        return self._num1 / self._num2
    
calculadora = Calculadora()
print("Suma: ", calculadora.suma())
print("Resta: ", calculadora.resta())
print("Multiplicación: ", calculadora.multiplicacion())
print("División: ", calculadora.division())
