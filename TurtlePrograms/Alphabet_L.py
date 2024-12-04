#Set Attributes
Background_color = input("Set your background color:")
Turtle_color = input("Set your pointer color:")
Pen_size = int(input("Set your pointer's size (in pixels):"))

import turtle
wn = turtle.Screen()
wn.bgcolor(Background_color)

#Configure Pointer/Turtle
my_turtle = turtle.Turtle()
my_turtle.color(Turtle_color)
my_turtle.pensize(Pen_size)

#initiate the alphabet
my_turtle.right(90)
my_turtle.forward(90)
my_turtle.left(90)
my_turtle.forward(60)
my_turtle.left(180)

wn.exitonclick()