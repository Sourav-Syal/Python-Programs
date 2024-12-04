import turtle
wn = turtle.Screen()
wn.bgcolor("turquoise")

my_turtle = turtle.Turtle()
my_turtle.shape("blank")
my_turtle.pensize(3)

for _ in range(5):
    my_turtle.left(72)
    my_turtle.forward(100)

wn.exitonclick()