class A():
    def __init__(self):
        self._contador = 0
        self._cuenta = 0
    @property #Es útil para que al llamar al getter de cuenta no tenamos que añadir los () 
    def cuenta(self):
        return self._cuenta

    @property
    def contador(self):
        return self._contador

a = A()
#print(a._cuenta)
#print(a.cuenta())
print(a.cuenta)
print(a.contador)