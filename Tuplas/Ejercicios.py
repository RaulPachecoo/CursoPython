#EJERCICIOS TUPLAS
#EJERCICIO 1

'''
Escribir una tupla con los meses del año, luego, pide al usuario un numero, 
el que haya ingresado, es el mes que debe mostrar en la tupla
'''

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

numero = int(input("Introduce el número de mes: "))

if numero < 1 or numero > 12:
    print("Ese número no corresponde a ningún mes")
else:
    print(meses[numero-1])

#EJERCICIO 2

'''
Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, 
el que haya ingresado, es la letra que debe imprimir el programa
'''

abecedario = tuple("abcdefghijklmnñopqrstuvwxyz")

numero = int(input("Introduce el número que corresponda a la letra que desees: "))

if numero < 1 or numero > 27:
    print("Ese número no corresponde a ninguna letra")
else:
    print(abecedario[numero-1])