import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.shape("turtle")

for i in range(4):
    t.fd(100)
    t.rt(90)

i = 0


resultado = input("¿Quieres imprimir una figura? ")
if resultado == "si":
    while i <= 100:
        t.circle(i)
        i += 10
else:
    print("Okay")

turtle.done()