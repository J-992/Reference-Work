
#im makingn a moon and person silhoutettwes

import turtle

bob = turtle.Turtle(shape = "turtle")
bib = turtle.Turtle(shape = "turtle")
blab = turtle.Turtle(shape = "turtle")
window = turtle.Turtle()
ray = turtle.Turtle(shape = "circle")
hill = turtle.Turtle(shape = "turtle")
wolf = turtle.Turtle(shape = "turtle")
name = turtle.Turtle(shape = "turtle")
star = turtle.Turtle(shape = "circle")
timer = turtle.Turtle()


# hiding the turtle for the words to show
window.hideturtle()
bob.hideturtle()
bib.hideturtle()
blab.hideturtle()
ray.hideturtle()
hill.hideturtle()
wolf.hideturtle()
name.hideturtle()
star.hideturtle()
timer.hideturtle()

window.hideturtle()
window.speed(5)
window.penup()
window.goto(-275,10)
window.write("please make the window fullscreen", font = ("Arial", 25))
window.goto(4200,2690)
window.penup()
window.hideturtle()
window.reset()


#speed(CHANGE??) - IN TESTING not anymore yay
bib.speed(5)
blab.speed(5)
bob.speed(7)
ray.speed(7)
hill.speed(7)
wolf.speed(10)
name.speed(5)
star.speed(4)
timer.speed(5)

#Making Background

bib.showturtle()

bib.penup()
bib.fillcolor("midnight blue")
bib.begin_fill()

bib.goto(-690,-390)
bib.pendown()
bib.goto(-690,390)
bib.goto(690,390)
bib.goto(690,-390)
bib.goto(-690,-390)

bib.end_fill()

bib.hideturtle()



#now doing moon light rays

ray.width(7)

#royal blue rays

ray.showturtle()

ray.fillcolor("royal blue")
ray.pencolor("royal blue")
ray.showturtle()

ray.penup()
ray.goto(-100, -340)
ray.pendown()

ray.begin_fill()
ray.circle(430)
ray.end_fill()

#cornflower blue rays

ray.fillcolor("cornflower blue")
ray.pencolor("cornflower blue")
ray.showturtle()

ray.penup()
ray.goto(-100, -310)
ray.pendown()

ray.begin_fill()
ray.circle(400)
ray.end_fill()

#light steel blue rays

ray.fillcolor("light steel blue")
ray.pencolor("light steel blue")
ray.showturtle()

ray.penup()
ray.goto(-100, -280)
ray.pendown()

ray.begin_fill()
ray.circle(370)
ray.end_fill()

ray.hideturtle()

#ground
blab.showturtle()

blab.fillcolor("black")
blab.showturtle()

blab.penup()
blab.goto(-690,-380)
blab.pendown()

blab.begin_fill()

blab.goto(-690,-230)
blab.goto(690,-230)
blab.goto(690, -390)
blab.goto(-690,-390)

blab.end_fill()

blab.hideturtle()

#1400x800px grid

#filling the border/drawing border

bob.showturtle()



bob.penup()
bob.goto(-730,-430)
bob.pendown()

bob.fillcolor("black")
bob.begin_fill()

bob.goto(-730,-430)
bob.goto(-730,430)
bob.goto(730,430)
bob.goto(730,-430)
bob.goto(-730,-430)

bob.penup()
bob.goto(-690,-390)
bob.pendown()

bob.goto(-690,390)
bob.goto(690,390)
bob.goto(690,-390)
bob.goto(-690,-390)

bob.end_fill()
bob.penup()

bob.hideturtle()

#moon
#moon circle
blab.showturtle()

blab.width(5)

blab.fillcolor("gainsboro")
blab.pencolor("gainsboro")


blab.penup()
blab.goto(-100,380)
blab.pendown()

blab.begin_fill()
blab.rt(180)
blab.circle(300)
blab.end_fill()


#crescent shadow part

blab.fillcolor("silver")
blab.pencolor("silver")

blab.penup()
blab.goto(-100,380)
blab.pendown()

blab.begin_fill()
blab.circle(300, 205)

blab.penup()
blab.goto(-100,380)
blab.pendown()

blab.rt(180)
blab.circle(300,155)
blab.end_fill()

#craters

blab.pencolor("silver")
blab.fillcolor("silver")

blab.shape("circle")

blab.penup()
blab.goto(-160,120)
blab.pendown()
blab.turtlesize(7,8)
blab.stamp()

blab.penup()
blab.goto(-210,290)
blab.pendown()
blab.turtlesize(5,5)
blab.stamp()

blab.penup()
blab.goto(-150, 120)
blab.pendown()
blab.stamp()

blab.penup()
blab.goto(-120,120)
blab.pendown()
blab.stamp()

blab.turtlesize(1, 2)
blab.penup()
blab.goto(-130, 200)
blab.stamp()

blab.penup()
blab.goto(-170, 250)
blab.pendown()
blab.stamp()

blab.penup()
blab.goto(-10, 10)
blab.pendown()
blab.turtlesize(5,10)
blab.stamp()

blab.penup()
blab.goto(20, 275)
blab.pendown()
blab.turtlesize(5,5,10)
blab.stamp()

blab.penup()
blab.goto(0,30)
blab.pendown()
blab.stamp()

blab.penup()
blab.goto(15,270)
blab.pendown()
blab.stamp()

blab.penup()
blab.goto(15,-100)
blab.pendown()
blab.stamp()

blab.penup()
blab.goto(20,-90)
blab.pendown()
blab.stamp()

blab.penup()
blab.goto(100, 150)
blab.pendown()
blab.stamp()

blab.turtlesize(1,1)

blab.hideturtle()

#done moon


#now making hill with person

hill.showturtle()

hill.fillcolor("black")
hill.pencolor("black")

hill.penup()

hill.goto(-100, -130)
hill.pendown()

hill.begin_fill()
hill.rt(80)
hill.fd(40)
hill.lt(50)
hill.fd(110)
hill.lt(30)
hill.fd(60)
hill.rt(45)
hill.fd(130)
hill.lt(45)
hill.fd(150)
hill.lt(130)
hill.fd(60)
hill.rt(30)
hill.fd(70)
hill.rt(80)
hill.fd(50)
hill.end_fill()


hill.hideturtle()


# making the person
#                       why did i make it named wolf idk howto make a wolf they v/ crappyyyyy



wolf.width(10)


wolf.pencolor("red")
wolf.fillcolor("red")

wolf.penup()
wolf.goto(50,-90)
wolf.pendown()

wolf.rt(110)
wolf.fd(65)

wolf.rt(120)
wolf.fd(30)

wolf.lt(120)
wolf.fd(40)

wolf.penup()
wolf.goto(42, -115)
wolf.pendown()

wolf.rt(50)
wolf.fd(30)

#head

wolf.pencolor("crimson")
wolf.fillcolor("red")

wolf.showturtle()

wolf.lt(150)

wolf.penup()
wolf.goto(50, -100)
wolf.pendown()

wolf.begin_fill()
wolf.circle(30)
wolf.end_fill()
wolf.hideturtle()

#stars

star.showturtle()

star.fillcolor("light cyan")
star.pencolor("light cyan")

star.turtlesize(0.5,0.5)

star.penup()
star.goto(330, 350)
star.pendown()
star.stamp()

star.penup()
star.goto(406, 340)
star.pendown()
star.stamp()

star.penup()
star.goto(-600, 340)
star.pendown()
star.stamp()

star.penup()
star.goto(-300, 340)
star.pendown()
star.stamp()

star.penup()
star.goto(-630, 300)
star.pendown()
star.stamp()

star.penup()
star.goto(610, 340)
star.pendown()
star.stamp()

star.penup()
star.goto(500, -43)
star.pendown()
star.stamp()

star.penup()
star.goto(650, 340)
star.pendown()
star.stamp()

star.penup()
star.goto(450, 340)
star.pendown()
star.stamp()

star.penup()
star.goto(600, 245)
star.pendown()
star.stamp()

star.penup()
star.goto(470, 355)
star.pendown()
star.stamp()

star.penup()
star.goto(620, 230)
star.pendown()
star.stamp()

star.penup()
star.goto(614, 140)
star.pendown()
star.stamp()

star.penup()
star.goto(670, -40)
star.pendown()
star.stamp()

#wave 2 of staers

star.penup()
star.goto(-330, 350)
star.pendown()
star.stamp()

star.penup()
star.goto(-406, 340)
star.pendown()
star.stamp()

star.penup()
star.goto(600, 340)
star.pendown()
star.stamp()

star.penup()
star.goto(300, 340)
star.pendown()
star.stamp()

star.penup()
star.goto(630, 300)
star.pendown()
star.stamp()

star.penup()
star.goto(-610,340)
star.pendown()
star.stamp()

star.penup()
star.goto(-500, 43)
star.pendown()
star.stamp()

star.penup()
star.goto(-650, 340)
star.pendown()
star.stamp()

star.penup()
star.goto(-450, 340)
star.pendown()
star.stamp()

star.penup()
star.goto(-600, 245)
star.pendown()
star.stamp()

star.penup()
star.goto(-470, 355)
star.pendown()
star.stamp()

star.penup()
star.goto(-620, 230)
star.pendown()
star.stamp()

star.penup()
star.goto(-614, 140)
star.pendown()
star.stamp()

#wave 3ree

star.penup()
star.goto(-670, 40)
star.pendown()
star.stamp()

star.penup()
star.goto(400, 40)
star.pendown()
star.stamp()

star.penup()
star.goto(-440, 50)
star.pendown()
star.stamp()

star.penup()
star.goto(-670, 90)
star.pendown()
star.stamp()

star.penup()
star.goto(-600, 100)
star.pendown()
star.stamp()

star.penup()
star.goto(-500, 40)
star.pendown()
star.stamp()



#wave 4

star.penup()
star.goto(670, -40)
star.pendown()
star.stamp()

star.penup()
star.goto(-400, -40)
star.pendown()
star.stamp()

star.penup()
star.goto(440, -50)
star.pendown()
star.stamp()

star.penup()
star.goto(300, -80)
star.pendown()
star.stamp()

star.penup()
star.goto(670, -90)
star.pendown()
star.stamp()

star.penup()
star.goto(600, -100)
star.pendown()
star.stamp()

star.penup()
star.goto(500, -40)
star.pendown()
star.stamp()

star.penup()
star.goto(200, -150)
star.pendown()
star.stamp()

star.hideturtle()


#name

timer.penup()
timer.goto(2000,2000)
timer.hideturtle()

name.penup()
name.goto(-590,350)
name.pendown()
name.pencolor("linen")
name.fillcolor("linen")
name.write("Jaffer Razavi", align="center",font=("Comis Sans MS", 30, "bold"))

#WOO IM DONE AYAAYAYJJSSJSJSJSJSJAJSJAJSAJSJASJASDJASDJWFWNFIERHFJFBAEFJAEF





