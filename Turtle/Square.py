import turtle

bob = turtle.Turtle()

bob.shape("turtle")

bob.penup()
bob.goto(-50,50)
bob.pendown()

bob.color("red")



bob.begin_fill()
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.end_fill()

bob.hideturtle()
bob.penup()
bob.goto(100,100)
bob.pendown()

bob.write("this is a square", font=('arial' '20'))
