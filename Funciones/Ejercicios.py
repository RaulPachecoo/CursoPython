#EJERCICIOS FUNCIONES

#EJERCICIO 1

'''
Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros 
al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros 
pares e impares dentro de dos listas nuevas
'''

lista = []
pares = []
impares = []

def llenarLista():
    n = 1
    while n != 0:
        n = int(input("Introduce un número (Salir = 0): "))
        if n != 0:
            lista.append(n)

def ordenarNumeros():
    lista.sort()
    for i in lista:  
        if i % 2 == 0:  
            pares.append(i)
        else:  
            impares.append(i)



llenarLista()
ordenarNumeros()


print("Lista completa:", lista)
print("Números pares:", pares)
print("Números impares:", impares)


#EJERCICIO 2

'''
Escribir una función que reciba un número entero positivo y devuelva su factorial.
'''

from math import factorial

def calcularFactorial(n):
    if n < 0:
        return "El número debe ser un entero positivo."
    return factorial(n)  


n = int(input("Introduce un número entero positivo: "))

if n >= 0:
    print("El factorial de {} es {}.".format(n, calcularFactorial(n)))
else:
    print("Por favor, introduce un número entero positivo.")


#EJERCICIO 3

'''
Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el programa debe retornar el valor 1; 
si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0
'''

def mayorDosNumeros():
    n1 = int(input("Introduce un número: "))
    n2 = int(input("Introduce otro número: "))

    if n1 > n2:
        return 1
    elif n2 > n1:
        return -1
    else:
        return 0


print(mayorDosNumeros())


#EJERCICIO 4

'''
Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
'''

def calcularFactura(cantidad, porcentajeIva = 21):
    total = 0
    cantidadIva = cantidad * porcentajeIva / 100

    total = cantidad + cantidadIva

    return total

print(calcularFactura(100, 7))


#EJERCICIO 5

'''
Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado 
con argumentos de base y altura; y la otra el area de un circulo con argumento de radio
'''

import math

def areaCuadrado(base, altura):
    return base * altura

def areaCirculo(radio):
    return math.pi * pow(radio, 2)

base = 2
altura = 2
radio = 2

print("Área de un cuadrado de base {} y altura {}: {}".format(base, altura, areaCuadrado(base, altura)))
print("Área de un círculo de radio {}: {}".format(radio, areaCirculo(radio)))



#EJERCICIO 6

'''
Escribir una función que reciba una muestra de números en una lista y devuelva su medida.
'''

def longitudListaNumeros(*numeros):
    return len(numeros)

print(longitudListaNumeros(1, 2, 3, 4, 5))