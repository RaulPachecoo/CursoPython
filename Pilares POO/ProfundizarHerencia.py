class Animales():
    def __init__(self, nombre):
        self._nombre = nombre

class Perro(Animales):
    def __init__(self, nombre, sonido):
        super().__init__(nombre)
        self._sonido = sonido


perro = Perro("Firulais", "Guuaaoo!")

print(perro._nombre)
print(perro._sonido)