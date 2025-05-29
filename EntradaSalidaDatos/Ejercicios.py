import math

# EJERCICIOS ENTRADA DE DATOS

# EJERCICIO 1

'''
Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, 
sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los 
valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre 
el mensaje: “La solución es: <solucion>”
'''
                    
a = float(input('Introduce el valor de a: '))
b = float(input('Introduce el valor de b: '))
c = float(input('Introduce el valor de c: '))

# Calcular el discriminante
discriminante = (b ** 2) - (4 * a * c)

# Verificar que el discriminante no sea negativo
if discriminante < 0:
    print("El discriminante es negativo. No hay soluciones reales.")
else:
    # Calcular las dos soluciones
    resultado1 = ((-b) + math.sqrt(discriminante)) / (2 * a)
    resultado2 = ((-b) - math.sqrt(discriminante)) / (2 * a)

    print("Las soluciones son:", resultado1, "y", resultado2)


# EJERCICIO 2

'''
Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido 
un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial 
y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final
'''

p1 = float(input('Introduce la nota de la práctica 1: '))
p2 = float(input('Introduce la nota de la práctica 2: '))
p3 = float(input('Introduce la nota de la práctica 3: '))

pp = (p1 + p2 + p3) / 3

ep = float(input('Introduce la nota del examen parcial: '))
ef = float(input('Introduce la nota del examen final: '))

promedio = (pp + 2*ep + 3*ef) / 6
10
print("El promedio del alumno es: ", promedio)


# EJERCICIO 3
'''
Escribir un programa que solicite al usuario un vocal en minuscula, 
y luego una letra en mayúsculas. El programa debe convertir la letra 
en minúscula y la vocal en mayúscula, y al final, 
deben ser concatenadas ambas
'''

consonante = input('Introduce una consonante mayúscula: ')
vocal = input('Introduce una vocal minúscula: ')

vocal = vocal.upper()
consonante = consonante.lower()

print("La consonante es: {} \nLa vocal es: {}".format(consonante, vocal))



# EJERCICIO 4
'''
Hacer un programa que pida al usuario su nombre, su edad y su sexo 
y los muestre de la siguiente forma:

Te llamas: <nombre>

Tu edad es: <edad>

Eres: <sexo>
'''

nombre = input('Introduce tu nombre: ')
edad = input('Introduce tu edad: ')
sexo = input('Introduce tu sexo: ')

print("Te llamas: {}\nTu edad es: {}\nEres: {}".format(nombre, edad, sexo))
