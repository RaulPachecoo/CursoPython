
# EJERCICIOS CONDICIONALES

# EJERCICIO 1

'''
Crear un programa que pida al usuario una letra, y si es vocal, 
muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal

'''

letra = input('Introduce una letra: ')

if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
    print("La", letra, "es vocal")
else:
    print("La", letra, "NO es vocal")

if letra.lower() in "aeiou":
    print("Es una vocal")
else:
    print("NO es una vocal")

# EJERCICIO 2

'''
Escribir un programa que, dado un número entero, muestre su valor absoluto. 
Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto 
de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado 
por -1 (el valor absoluto de -52 es 52).

'''

n = int(input("Introduce un número: "))

if n >= 0:
    print("El valor absoluto del número introducido es:", n)
elif n<0:
    print("El valor absoluto del número introducido es:", (n*(-1)))


# EJERCICIO 3

'''
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas
letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman 
un poco y si no, que no riman.
'''

palabra1 = input('Introduce una palabra: ')
palabra2 = input('Introduce otra palabra: ')

if len(palabra1) < 3 or len(palabra2) < 3:
    print("NO rima, porque tienen menos de 3 letras")
elif palabra1[-3 : ] == palabra2[-3 : ]:
    print("Las palabras riman")
elif palabra1[-2 : ] == palabra2[-2 : ]:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")


# EJERCICIO 4

'''
Crear un programa que permita al usuario elegir un candidato por el cual votar. 
Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, 
candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir 
el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. 
Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos 
disponibles, indicar “Opción errónea”.
'''

print("Partido Rojo: A \nPartido Verde: B \nPartido Azul: C")
voto = input("Introduce el partido al que quieras votar: ")

if voto.upper() == "A":
    print("Usted ha votado por el partido Rojo")
elif voto.upper() == "B":
    print("Usted ha votado por el partido Verde")
elif voto.upper() == "C":
    print("Usted ha votado por el partido Azul")
else:
    print("Opción errónea")