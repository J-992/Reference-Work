import turtle

bob = turtle.Turtle()
bob.shape("turtle")

bob.hideturtle()

bob.speed(10)

bob.begin_fill()
bob.circle(10)
bob.end_fill()
bob.circle(20)

bob.pencolor("white")
bob.forward(50)

bob.pencolor("black")
bob.begin_fill()
bob.circle(10)
bob.end_fill()
bob.circle(20)

bob.right(180)
bob.pencolor("white")
bob.forward(25)
bob.left(90)
bob.forward(50)

bob.pencolor("black")
bob.right(90)
bob.forward(50)
bob.right(50)
bob.forward(25)
bob.right(180)
bob.forward(25)
bob.left(50)
bob.forward(100)
bob.left(50)
bob.forward(25)
bob.left(180)
bob.forward(25)
bob.right(50)
bob.forward(50)
bob.left(90)
bob.pencolor("white")
bob.forward(100)

bob.pencolor("black")
bob.left(90)
bob.circle(200)
bob.right(90)

bob.pencolor("white")
bob.forward(100)
bob.pencolor("black")

bob.write("i am autism", font=('arial',20,"bold"))


