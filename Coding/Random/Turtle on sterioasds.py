import turtle
import random

tur = turtle.Turtle(shape='turtle',undobuffersize=10)
tur.speed(0)
scr = turtle.Screen()
scr.colormode(255)
squ = turtle.Turtle()
squ.speed(0)
epilepsy = turtle.Turtle()
epilepsy.speed(0)

cordx = 0
cordy = 0

squx = 0
squy = 0

tur.hideturtle()
squ.hideturtle()
epilepsy.hideturtle()

def main():
    for x in range (1000):
#        epilepsy.fillcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
 #       epilepsy.begin_fill()
  #      epilepsy.goto(-700,400)
   #     epilepsy.goto(-700,-400)
    #    epilepsy.goto(700,-400)
     #   epilepsy.goto(700,400)
      #  epilepsy.end_fill()
        cordx = random.randint(-600,600)
        cordy = random.randint(-600,600)
        tur.penup()
        tur.goto(cordx,cordy)
        tur.pendown()
        tur.fillcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        tur.begin_fill()
        tur.circle(20)
        tur.end_fill()
        squx = random.randint(-600,600)
        squy = random.randint(-600,600)
        squ.penup()
        squ.fillcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        squ.goto(squx,squy)
        squ.pendown()
        squ.begin_fill()
        squ.fd(10)
        squ.rt(90)
        squ.fd(10)
        squ.rt(90)
        squ.fd(10)
        squ.rt(90)
        squ.fd(10)
        squ.rt(90)
        squ.fd(10)
        squ.rt(90)
        squ.end_fill()
        x=x-1
        main()
main()
