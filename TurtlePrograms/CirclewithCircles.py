import turtle

wn = turtle.Screen()
wn.bgcolor("black")
my_turtle = turtle.Turtle()
my_turtle.shape("circle")

my_turtle.color("Dark Green","yellow")
my_turtle.penup()
my_turtle.goto(50.00,50.00)
my_turtle.speed(10)

for _ in range(15):
  my_turtle.stamp()
  my_turtle.forward(50)
  my_turtle.stamp()
  my_turtle.right(24)
  my_turtle.backward(20)

wn.exitonclick()