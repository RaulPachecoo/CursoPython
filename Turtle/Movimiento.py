import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.goto(100, 100) #Para que la tortuga vaya a las coordenadas especificadas
t.goto(-100, 100)
#t.goto(0, 0) La tortuga vuelve al punto de partida
t.home() #La tortuga vuelve al punto de partida

t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)


turtle.done()