diccionario = {1 : 2, 2 : 3, 3 : 4}

print(diccionario)
# Elimina el elemento con la llave = 3
diccionario.pop(3)
print(diccionario)

# Vacía el diccionario
diccionario.clear()
print(diccionario)

diccionario = {1 : 2, 2 : 3, 3 : 4}

# Saca el elemento con la llave = 2
print(diccionario.get(2))

# Añade al final un elemento con llave = 4 y valor = 5
diccionario.setdefault(4 , 5)
print(diccionario)

diccionario2 = {5 : 6, 6 : 7}
# Fusiona los dos diccionarios
diccionario.update(diccionario2)
print(diccionario)

# Realiza una copia del diccionario
diccionario.copy()
print(diccionario)
