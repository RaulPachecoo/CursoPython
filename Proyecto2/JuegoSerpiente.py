import turtle
import time
import random
import winsound  # Importar para los sonidos

# Inicializar variables
retraso = 0.2  # Velocidad inicial más lenta
marcador = 0
marcadorAlto = 0
comidas_contador = 0  # Contador para calcular la disminución progresiva

# Configuración de la ventana
s = turtle.Screen()
s.setup(750, 750)
s.bgcolor("black")
s.title("JUEGO DE LA SERPIENTE")

# Configuración de la serpiente
serpiente = turtle.Turtle()
serpiente.speed(5)
serpiente.shape("square")
serpiente.penup()
serpiente.goto(0, 0)
serpiente.direction = 'stop'
serpiente.color("green")

# Configuración de la comida
comida = turtle.Turtle()
comida.shape('circle')
comida.color('orange')
comida.penup()
comida.goto(0, 100)
comida.speed(0)

# Segmentos del cuerpo de la serpiente
cuerpo = []

# Configuración del marcador
texto = turtle.Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Puntuación: 0\tPuntuación más alta: 0", align="center", font=("verdana", 24, "normal"))

# Funciones para el movimiento de la serpiente
def arriba():
    if serpiente.direction != 'down':
        serpiente.direction = 'up'

def abajo():
    if serpiente.direction != 'up':
        serpiente.direction = 'down'

def derecha():
    if serpiente.direction != 'left':
        serpiente.direction = 'right'

def izquierda():
    if serpiente.direction != 'right':
        serpiente.direction = 'left'

def movimiento():
    if serpiente.direction == 'up':
        y = serpiente.ycor()
        serpiente.sety(y + 20)
    if serpiente.direction == 'down':
        y = serpiente.ycor()
        serpiente.sety(y - 20)
    if serpiente.direction == 'right':
        x = serpiente.xcor()
        serpiente.setx(x + 20)
    if serpiente.direction == 'left':
        x = serpiente.xcor()
        serpiente.setx(x - 20)

def reiniciar_juego():
    global marcador, retraso, comidas_contador
    texto.goto(0, 0)
    texto.write("\u00a1Game Over!", align="center", font=("verdana", 36, "normal"))
    time.sleep(2)
    texto.clear()
    texto.goto(0, 260)
    for segmento in cuerpo:
        segmento.clear()
        segmento.hideturtle()
    serpiente.home()
    serpiente.direction = 'stop'
    cuerpo.clear()

    marcador = 0
    comidas_contador = 0  # Reiniciar el contador de comidas
    retraso = 0.2  # Reiniciar la velocidad
    texto.write("Puntuaci\u00f3n: {}\tPuntuaci\u00f3n m\u00e1s alta: {}".format(marcador, marcadorAlto), align="center", font=("verdana", 24, "normal"))

# Configuración de los controles
s.listen()
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")

# Bucle principal del juego
while True:
    s.update()

    # Verificar colisión con los bordes
    if serpiente.xcor() > 350 or serpiente.xcor() < -350 or serpiente.ycor() > 350 or serpiente.ycor() < -350:
        reiniciar_juego()

    # Verificar colisión con la comida
    if serpiente.distance(comida) < 20:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        comida.goto(x, y)

        winsound.PlaySound("comida.wav", winsound.SND_ASYNC)

        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape('square')
        nuevo_cuerpo.color('green')
        nuevo_cuerpo.penup()
        cuerpo.append(nuevo_cuerpo)

        marcador += 10
        if marcador > marcadorAlto:
            marcadorAlto = marcador

        texto.clear()
        texto.write("Puntuaci\u00f3n: {}\tPuntuaci\u00f3n m\u00e1s alta: {}".format(marcador, marcadorAlto), align="center", font=("verdana", 24, "normal"))

        # Incrementar la velocidad reduciendo el retraso progresivamente
        comidas_contador += 1
        retraso = max(0.05, retraso - comidas_contador * 0.5)

    # Mover el cuerpo de la serpiente
    total = len(cuerpo)
    for index in range(total - 1, 0, -1):
        x = cuerpo[index - 1].xcor()
        y = cuerpo[index - 1].ycor()
        cuerpo[index].goto(x, y)

    if total > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x, y)

    # Movimiento de la serpiente
    movimiento()

    # Verificar colisión con el cuerpo
    for segmento in cuerpo:
        if segmento.distance(serpiente) < 20:
            reiniciar_juego()

    time.sleep(retraso)

turtle.done()
