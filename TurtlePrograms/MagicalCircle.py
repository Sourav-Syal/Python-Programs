import turtle
wn = turtle.Screen()
wn.bgcolor("black")

my_turtle = turtle.Turtle()
my_turtle.shape("blank")
my_turtle.color("turquoise")

for _ in range(46):
     my_turtle.speed(10)
     my_turtle.forward(50)
     my_turtle.stamp()
     my_turtle.backward(50)
     my_turtle.right(8)

my_turtle.penup()
my_turtle.goto(150,150)
my_turtle.pendown()
my_turtle.color("green")
for _ in range(46):
     my_turtle.speed(10)
     my_turtle.forward(50)
     my_turtle.stamp()
     my_turtle.backward(50)
     my_turtle.right(8)

my_turtle.penup()
my_turtle.goto(-150,150)
my_turtle.pendown()
my_turtle.color("orange")
for _ in range(46):
     my_turtle.speed(10)
     my_turtle.forward(50)
     my_turtle.stamp()
     my_turtle.backward(50)
     my_turtle.right(8)

my_turtle.penup()
my_turtle.goto(-150,-150)
my_turtle.pendown()
my_turtle.color("grey")
for _ in range(46):
     my_turtle.speed(10)
     my_turtle.forward(50)
     my_turtle.stamp()
     my_turtle.backward(50)
     my_turtle.right(8)

my_turtle.penup()
my_turtle.goto(150,-150)
my_turtle.pendown()
my_turtle.color("white")
for _ in range(46):
     my_turtle.speed(10)
     my_turtle.forward(50)
     my_turtle.stamp()
     my_turtle.backward(50)
     my_turtle.right(8)

wn.exitonclick()
