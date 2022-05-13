"""
Author 1: Rodrigo García Estrada
Author 2: Misael Chávez
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Variables con el hexadecimal de 6 colores diferentes
cyan = '#00FFFF'
ladrillo = '#FF4D00'
rosa = '#FFB0D8'
amarilo = '#FFDF00'
morado = '#B700FF'
botella = '#007974'

#lista de los colores y asignacion aleatoria de estos a la comida y serpiente
randomcolor = [botella,cyan,ladrillo,rosa,amarilo,morado]
snakecolor = randomcolor[randrange(0, 6)]
foodcolor = randomcolor[randrange(0, 6)]



def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    #sumar a ta x de food 10 pixeles
    #Se mueve la comida 10 pixeles, en caso de estar cerca de una de las paredes no se movera hacia esa diraccion
    if (food.x == -150):
        if head != food:
            movefood = randrange(1, 40)
            if movefood == 10:
                food.x += 10
            elif movefood == 20:
                food.y += 10
            elif movefood == 30:
                food.x -= 10
            else:
                food.x = food.x
    elif (food.x == 140):
        if head != food:
            movefood = randrange(1, 40)
            if movefood == 10:
                food.y += 10
            elif movefood == 30:
                food.y -=10
            elif movefood == 20:
                food.x -= 10
            else:
                food.x = food.x
    elif (food.y == -150):
        if head != food:
            movefood = randrange(1, 40) 
            if movefood == 10:
                food.x += 10
            elif movefood == 20:
                food.y += 10
            elif movefood == 30:
                food.x -= 10
            else:
                food.x = food.x
    elif (food.y == 140):
        if head != food:
            movefood = randrange(1, 40)
            if movefood == 10:
                food.x += 10
            elif movefood == 20:
                food.y -= 10
            elif movefood == 30:
                food.x -= 10
            else:
                food.x = food.x
    else:
        if head != food:
            movefood = randrange(1, 40)
            if movefood == 10:
                food.x += 10
            elif movefood == 20:
                food.y -= 10
            elif movefood == 39:
                food.y += 10
            elif movefood == 30:
                food.x -= 10
            else:
                food.x = food.x

    clear()
# Se cambio el color predeterminado de la serpiente por el aleatoria que se cambio arriba;
# se hace algo de manera similar con la comida
    for body in snake:
        square(body.x, body.y, 9, snakecolor)

    square(food.x, food.y, 9, foodcolor)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
