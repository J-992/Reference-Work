import turtle

red = turtle.Turtle()
bob = turtle.Turtle()

bob.shape("turtle")
red.shape("turtle")
bob.speed(100)
red.fillcolor("red")

bob.penup()
bob.goto(200,200)
bob.pendown()
bob.fillcolor("blue")
bob.pencolor("red")
red.pencolor("blue")


#while True:
  #  for e in range(10):
     #   red.forward(40)
      #  red.right(40)
       # bob.forward(70)
        #bob.right(40)
        
   # red.left(30)
   # bob.left(30)


for i in range(200):
    red.forward(10)
    red.right(40)
    bob.forward(20)
    bob.right(40)

    red.left(30)
    bob.left(20)
    








