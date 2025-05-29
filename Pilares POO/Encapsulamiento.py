class A(): 
    def __init__(self):
        self.contador = 0

    def incrementar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador
    
class B():
    #Al añadir __ hace un atributo privado
    def __init__(self):
        self.__contador = 0

    def incrementar(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador


print("Objeto 1")
a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())
print(a.contador)

print("Objeto 2")
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
# print(b.__contador) Da error ya que no se puede acceder directamente a un atributo privado