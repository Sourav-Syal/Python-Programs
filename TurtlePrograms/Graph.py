Background_color = input("Set your background color:")
Length1 = int(input("Set Length of your x-axis:"))
Length2 = int(input("Set Length of your y-axis:"))
Length3 = int(input("Set Length of your z-axis:"))
Length4 = int(input("Set Length of your s-axis:"))

import turtle

#Instance of Scree Class
wn = turtle.Screen()
wn.bgcolor(Background_color)

#Instance of Turtle Class
x_axis = turtle.Turtle()
y_axis = turtle.Turtle()
z_axis = turtle.Turtle()
s_axis = turtle.Turtle()

x_axis.pensize(5)
y_axis.pensize(5)
z_axis.pensize(5)
s_axis.pensize(5)

x_axis.forward(Length1)
x_axis.right(180)
x_axis.forward(Length1 * 2)

y_axis.left(90)
y_axis.forward(Length2)
y_axis.right(180)
y_axis.forward(Length2 * 2)

s_axis.left(135)
s_axis.forward(Length4)
s_axis.right(180)
s_axis.forward(Length4 * 2)

z_axis.right(135)
z_axis.forward(Length3)
z_axis.right(180)
z_axis.forward(Length3 * 2)

wn.exitonclick()