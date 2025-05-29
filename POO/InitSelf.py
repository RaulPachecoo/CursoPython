#Init es el constructor en Python
#Self es igual a This, e incluso también se podría usar This
class FabricaTelefonos():
    
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color


    def elaborarHuawei(self):
        self.marca = "Huawei"


telefono = FabricaTelefonos("Samsung", "Negro")

print(telefono.marca)

telefono.elaborarHuawei()

print(telefono.marca)