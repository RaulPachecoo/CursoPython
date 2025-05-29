'''
def <nombre de la función>(Parámetros):
    <sentencias>
'''

def saludo():
    print("Hola Raúl")

saludo()

def tabla7():
    resultado = 0
    for i in range(11):
        resultado = 7 * i
        print("7 x {} = {}".format(i, resultado))


tabla7()

def asignacion():
    return 1, 2, 3, 4, 5

a, b, c, d, e = asignacion()

print(a, b, c, d, e)