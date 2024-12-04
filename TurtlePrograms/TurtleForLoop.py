Background_color = input("Set your background color:")
Turtle_color = input("Set your pointer color:")
Pen_size = int(input("Set your pointer's size (in pixels):"))

import turtle

wn = turtle.Screen()                     #Initiate Screen
wn.bgcolor(Background_color)             #Set Screen Color

my_turtle = turtle.Turtle()              #Initiate Turtle
my_turtle.color(Turtle_color)            #Set Turtle Color
my_turtle.pensize(Pen_size)              #Set Turtle Width

angle = 60
distance = 60

for _ in range(6):                       #for loop initiated
    my_turtle.right(angle)
    my_turtle.forward(distance)
    angle+=60
    distance+=20                         #for loop ended, block completed

my_turtle.left(90)
my_turtle.forward(105)
my_turtle.left(90)
my_turtle.forward(270)

wn.exitonclick()