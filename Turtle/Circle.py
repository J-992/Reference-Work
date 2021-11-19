import turtle

bob = turtle.Turtle()

bob.shape("turtle")


bob.penup()
bob.goto(0,-50)
bob.pendown()

bob.begin_fill()
bob.circle(50)
bob.end_fill()
