conjunto = {1, 2, 3, 4, 5}

print(conjunto)

conjunto.add(20)
print(conjunto)

conjunto.remove(1)
print(conjunto)

conjunto.discard(20)
print(conjunto)

# pop() en los conjuntos, coge un elemento al azar y lo elimina
conjunto.pop()
print(conjunto)

#Añade elementos al conjunto, pero no al final sino al azar
conjunto.update([1, 2])
print(conjunto)

conjunto.clear()
print(conjunto)
