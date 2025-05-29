class A():
    def __init__(self):
        # _ significa privado entre programadores aunque Python te permite acceder a ellos desde fuera 
        self._contador = 0
        self._cuenta = 0

    def incrementar(self):
        self._contador += 1

    def cuenta(self):
        return self._contador
    

a = A()
print(a._cuenta)
a._cuenta = 20
print(a._cuenta)
# print(a.cuenta)
# a.cuenta = 20
# print(a.cuenta)


    
