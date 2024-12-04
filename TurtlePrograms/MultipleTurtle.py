Background_Color = input("Enter Screen Background Color:")
Turtle_Color = input("Enter the color of turtle/pointer:")
Pen_Size = int(input("Enter the width of your pointer:"))

import turtle

#Initializing Class Instance
#Turtle Screen Object
wn = turtle.Screen()
wn.bgcolor(Background_Color)    #Setting Background Color Attribute

#Turtle Object
alex = turtle.Turtle()
alex.color(Turtle_Color)              #Setting turtle color
alex.pensize(Pen_Size)                #Setting turtle width

tess = turtle.Turtle()
tess.pensize(Pen_Size)

#Calling Method for Alex
alex.forward(80)
alex.left(120)
alex.forward(80)
alex.left(120)
alex.forward(80)
alex.left(120)

#Calling Method for Tess
tess.forward(100)
tess.left(90)
tess.forward(75)
tess.left(90)
tess.forward(100)
tess.left(90)
tess.forward(75)
tess.left(90)

wn.exitonclick()