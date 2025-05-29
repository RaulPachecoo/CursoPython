#EJERCICIOS BUCLES

#EJERCICIO 1

'''
Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero
'''

numero = int(input("Introduce un número: "))

print("Tabla de multiplicar de {}:".format(numero))

i = 0
while i <= 10:
    resultado = numero * i
    print("{} x {} = {}".format(numero, i, resultado))
    i += 1 


#EJERCICIO 2

'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''

edad = int(input("Introduce tu edad: "))

i = 0
while i < edad:
    i += 1
    print("Has cumplido {}".format(i))
    



#EJERCICIO 3

'''
Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros 
y mostrar el rango de numeros entre ambas cifras
'''

for i in range(1, 11):
    print(i)

numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número mayor al anterior: "))

if numero2 <= numero1:
    print("Te he dicho que el segundo número tiene que ser mayor, deslenguado")
else:
    for i in range(numero1, numero2 + 1):
        print(i)



#EJERCICIO 4

'''
Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango 
de esos 2 números, pero, solo imprimiendo los números que sean impares
'''
numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número mayor al anterior: "))

if numero2 <= numero1:
    print("Te he dicho que el segundo número tiene que ser mayor, deslenguado")
else:
    print("Los números impares en ese rango son: ")
    for i in range(numero1, numero2 + 1):
        if i % 2 == 0:
            continue
        print(i)
