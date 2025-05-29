import turtle

s = turtle.Screen()
t = turtle.Turtle()

'''
t.begin_fill() # Comienzza el rellenado
t.circle(100)
t.end_fill() # Finaliza el rellenado

t.begin_fill()
t.color("white", "white")
t.circle(50)
t.end_fill()
'''

t.shape("turtle") #Cambia la forma del puntero a una tortuga
t.fd(100)
t.penup() #Levanta el lápiz
t.fd(50)
t.pendown() #Vuelve a poner el lápiz sobre el lienzo para pintar
t.fd(100)

t.undo() #Retroceso, es decir un ctrl + z
t.clear() #Limpia toda la pantalla
t.reset() #Reinica el programa

t.fd(100)
t.stamp() #Deja una marca de agua/sello
t.fd(100 )

turtle.done()