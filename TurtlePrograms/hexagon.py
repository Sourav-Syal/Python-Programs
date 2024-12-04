import turtle
wn = turtle.Screen()
wn.bgcolor("turquoise")

my_turtle = turtle.Turtle()
my_turtle.shape("blank")
my_turtle.pensize(3)
my_turtle.penup()
my_turtle.goto(50.00,0.00)
my_turtle.pendown()

for _ in range(6):
    my_turtle.left(60)
    my_turtle.forward(100)

wn.exitonclick()