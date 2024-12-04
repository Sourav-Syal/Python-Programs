import turtle
wn = turtle.Screen()
wn.bgcolor("turquoise")

my_turtle = turtle.Turtle()
my_turtle.shape("blank")
my_turtle.pensize(3)
my_turtle.up()
my_turtle.goto(10.00,-50.00)
my_turtle.down()

for _ in range(8):
    my_turtle.left(45)
    my_turtle.forward(100)

wn.exitonclick()