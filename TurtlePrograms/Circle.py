import turtle
wn = turtle.Screen()
beta = turtle.Turtle()

beta.speed(10)
for _ in range(100):
    for i in range(13):
        beta.forward(i)
        beta.left(i)

wn.exitonclick()