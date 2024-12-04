import turtle
wn = turtle.Screen()
wn.bgcolor("black")

my_turtle = turtle.Turtle()
my_turtle.shape("circle")
my_turtle.color("turquoise")

speed = 0
dist = 10

for _ in range(30):
     my_turtle.speed(speed)
     my_turtle.penup()
     my_turtle.up()
     my_turtle.stamp()
     my_turtle.forward(dist)
     my_turtle.right(90)
     dist+=2
     speed+=10

wn.exitonclick()
