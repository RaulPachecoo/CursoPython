import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.speed(10) #Velocidad de la tortuga dibujando (10 Máximo y 1 Mínimo)
t.circle(10) #La tortuga dibuja un círculo del radio especificado
t.circle(50)
t.dot(30) #La tortuga dibuja un punto del diámetro especificado

t.hideturtle() #Oculta la tortuga
t.circle(40)
t.showturtle() #Muestra la tortuga
t.circle(100)

t.setx(100) #Igual que goto pero mueve la tortuga en el eje x
t.sety(-300) #Igual que goto pero mueve la tortuga en el eje y

turtle.done()