import turtle

bob = turtle.Turtle()

bob.shape("turtle")

bob.penup()
bob.goto(0,50)
bob.pendown()

bob.color("blue")
bob.begin_fill()
bob.circle(50,360,6)
bob.end_fill()

#the last number in the bob.circle command is the number of sides in the shape.
