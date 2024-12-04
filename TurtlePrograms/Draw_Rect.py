Width = int(input("Enter Width of your rectangle:"))
Length = int(input("Enter Length of your rectangle:"))
Background_color = input("Set your background color:")
Turtle_color = input("Set your pointer color:")
Pen_size = int(input("Set your pointer's size (in pixels):"))

import turtle

#Set Instance
wn = turtle.Screen()
wn.bgcolor(Background_color)

my_turtle = turtle.Turtle()
my_turtle.color(Turtle_color)
my_turtle.pensize(Pen_size)

my_turtle.forward(Width)                 #Start to create a rectangle
my_turtle.left(90)
my_turtle.forward(Length)
my_turtle.left(90)
my_turtle.forward(Width)
my_turtle.left(90)
my_turtle.forward(Length)                #Completed the rectangle

my_turtle.left(90)                       #Pointing the direction from started

wn.exitonclick()