import turtle

bob = turtle.Turtle()

bob.shape("turtle")
bob.speed(speed=1)

bob.begin_fill()
bob.color("yellow")
bob.circle(50)
bob.end_fill()

bob.goto(40,60)

bob.color("black")
bob.shape("circle")
bob.stamp()
bob.right(180)

bob.penup()
bob.forward(50)
bob.pendown()
bob.stamp()
bob.penup()
bob.goto(20,30)
bob.pendown()
bob.color("red")
bob.begin_fill()
bob.forward(30)
bob.left(90)
bob.circle(20,180)
bob.end_fill()
bob.hideturtle()
bob.penup()
bob.goto(-20,10)



