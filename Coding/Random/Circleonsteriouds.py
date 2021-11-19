#jaffer Razavi

import turtle

bob = turtle.Turtle()
bib = turtle.Turtle()
bub = turtle.Turtle()
bab = turtle.Turtle()

bob.speed(0)
bib.speed(0)
bub.speed(0)
bab.speed(0)


bib.rt(180)
bub.rt(90)
bab.lt(90)

for i in range (0,900,3):
    bob.circle(1+i)
    bib.circle(1+i)
    bub.circle(1+i)
    bab.circle(1+i)
