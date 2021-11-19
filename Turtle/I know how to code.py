import turtle

bob = turtle.Turtle()



bob.shape("turtle")

#square

bob.penup()
bob.goto(-250,-220)
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
bob.goto(-190,-190)


bob.write("this is a square", font=('arial' '20'))




#circle

bob.color("grey")

bob.showturtle()
bob.penup()
bob.goto(250,-250)
bob.pendown()

bob.begin_fill()
bob.circle(50)
bob.end_fill()

bob.hideturtle()
bob.penup()
bob.goto(120,-190)


bob.write("this is a circle", font=('arial' '20'))



#hexagon
bob.color("purple")
bob.penup()
bob.goto(-250,250)
bob.pendown()

bob.color("blue")
bob.begin_fill()
bob.circle(50,360,6)
bob.end_fill()

bob.hideturtle()
bob.penup()
bob.goto(-190,190)


bob.write("this is a hexagon", font=('arial' '20'))

#the last number in the bob.circle command is the number of sides in the shape.



#star
bob.color("black")
bob.penup()
bob.goto(250,250)
bob.pendown()
bob.begin_fill()
bob.forward(100)
bob.right(144)
bob.forward(100)
bob.right(144)
bob.forward(100)
bob.right(144)
bob.forward(100)
bob.right(144)
bob.forward(100)
bob.right(144)
bob.end_fill()
bob.penup()
bob.goto(50,50)
bob.pendown()

bob.hideturtle()
bob.penup()
bob.goto(190,190)


bob.write("this is a star", font=('arial' '20'))

#angle of a star is 144 degrees i thinkkkkkkk



#happy face
bob.showturtle()
bob.goto(0,0)
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

bob.hideturtle()
bob.penup()
bob.goto(70,70)


bob.write("this is a happy face", font=('arial' '20'))


