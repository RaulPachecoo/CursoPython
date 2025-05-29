
# EJERCICIOS OPERADORES ARITMÉTICOS

# EJERCICIO 1

resultado = ((3 + 2) / (2 * 5)) ** 2
# resultado = pow(((3 + 2) / (5 * 2)) , 2)
print(resultado)

# EJERCICIO 2

cantidadPayasos = 23
cantidadMuñecas = 54

pesoPayaso = 112
pesoMuñena = 75

pesoTotal = (cantidadPayasos * pesoPayaso) + (cantidadMuñecas * pesoMuñena)
print("El peso total del paquete es ", pesoTotal, " gramos")


# EJERCICIOS CADENAS DE TEXTO

# EJERCICIO 1

cadena = "Te quiero solo como amigo"

print(cadena[ : 2])
print(cadena[-3 : ])

print(cadena[: : 2])
print(cadena[: : -1])
print(cadena + cadena[: : -1])


# EJERCICIO 2

palabra = "eparado"
caracter = ","

print("S" + palabra.replace("", ","))