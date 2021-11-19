#jaffer Razavi
#oct 20,2019

import turtle
import random

bob = turtle.Turtle()

bob.hideturtle()

bob.speed(0)

for i in range (40):
    Xcord = random.randint(-400,400)
    Ycord = random.randint(-400,400)
    Radius = random.randint(20,40)
    bob.penup()
    bob.goto(Xcord,Ycord)
    bob.pendown()
    bob.circle(Radius)
