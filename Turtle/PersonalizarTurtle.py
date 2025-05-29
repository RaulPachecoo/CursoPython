import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor("red") # Cambia el color del lienzo
s.title("Proyecto 1") # Cambia el título de la pantalla

t.shapesize(10, 5, 1) # Cambia el tamaño de la tortuga (width, height, border)
t.shapesize(5, 10, 1)
t.shapesize(3, 3, 3)

t.fillcolor("orange") # Cambia el color de la tortuga
t.fd(100)

t.pencolor("white") # Cambia tanto el color del borde como el color del lápiz
t.fd(100)

t.color("green", "blue") # Cambia el color de la tortuga y el color del lápiz
t.rt(90)
t.fd(100)

t.pensize(5) # Cambia el tamaño del lápiz
t.forward(100)

turtle.done()