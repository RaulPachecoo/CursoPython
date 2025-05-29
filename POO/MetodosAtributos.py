class FabricaTelefonos():
    marca = "Huawei"
    color = "Negro"
    memoriaRam = 32
    almacenamiento = 128

    def llamar(self, mensaje):
        return mensaje
    
    def escucharMusica(self):
        print("Estás escuchando Música")


telefono = FabricaTelefonos()

print(telefono.marca)
print(telefono.color)

print(telefono.llamar("Hola, ¿Con quién hablo?"))
telefono.escucharMusica()