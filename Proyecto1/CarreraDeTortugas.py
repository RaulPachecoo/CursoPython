import turtle
import random

s = turtle.Screen()
s.title("Carrera de tortugas")
s.bgcolor("#F5DEB3")

jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()
jugador3 = turtle.Turtle()

jugador1.hideturtle()
jugador1.shape("turtle")
jugador1.color("green", "green")
jugador1.shapesize(2, 2, 2)
jugador1.pensize(3)

jugador2.hideturtle()
jugador2.shape("turtle")
jugador2.color("blue", "blue")
jugador2.shapesize(2, 2, 2)
jugador2.pensize(3)

jugador3.hideturtle()
jugador3.shape("turtle")
jugador3.color("orange", "orange")
jugador3.shapesize(2, 2, 2)
jugador3.pensize(3)

jugador1.penup()
jugador1.goto(240, 150)
jugador1.pendown()
jugador1.circle(40)

jugador1.penup()
jugador1.goto(-240, 190)
jugador1.showturtle()

jugador2.penup()
jugador2.goto(240, 0)
jugador2.pendown()
jugador2.circle(40)

jugador2.penup()
jugador2.goto(-240, 40)
jugador2.showturtle()

jugador3.penup()
jugador3.goto(240, -150)
jugador3.pendown()
jugador3.circle(40)

jugador3.penup()
jugador3.goto(-240, -110)
jugador3.showturtle()

dado = [1, 2, 3, 4, 5, 6] 

for i in range(20):
    if jugador1.xcor() >= 240:
        print("¡LA TORTUGA VERDE HA GANADO!")
        break
    elif jugador2.xcor() >= 240:
        print("¡LA TORTUGA AZUL HA GANADO!")
        break
    elif jugador3.xcor() >= 240:
        print("¡LA TORTUGA NARANJA HA GANADO!")
        break
    else:
        turno1 = input("JUGADOR 1 presiona la tecla ENTER para avanzar.")
        turno1 = random.choice(dado)
        print("Tu número es: ", turno1, "\nAvanzas: ", turno1 * 20)
        jugador1.pendown()
        jugador1.forward(20*turno1)

        turno2 = input("JUGADOR 2 presiona la tecla ENTER para avanzar.")
        turno2 = random.choice(dado)
        print("Tu número es: ", turno2, "\nAvanzas: ", turno2 * 20)
        jugador2.pendown()
        jugador2.forward(20*turno2)

        turn3 = input("JUGADOR 3 presiona la tecla ENTER para avanzar.")
        turno3 = random.choice(dado)
        print("Tu número es: ", turno3, "\nAvanzas: ", turno3 * 20)
        jugador3.pendown()
        jugador3.forward(20*turno3)

turtle.done()