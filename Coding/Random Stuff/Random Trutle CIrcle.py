import turtle
import random

bob = turtle.Turtle(shape="turtle")
bob.speed(-10)

Col = ' '
Cir = random.randint(1,4)

if (Cir == 1):
    Col = "red"
elif (Cir == 2):
    Col = "green"
elif (Cir == 3):
    Col = "blue"
else:
    Col = "yellow"

bob.fillcolor(Col)
bob.begin_fill()
bob.circle(40,360)
bob.end_fill()

