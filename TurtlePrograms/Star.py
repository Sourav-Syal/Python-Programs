import turtle
wn = turtle.Screen()
ben = turtle.Turtle()

angle = (180-36) / 2
distance = 100

ben.speed(1)
ben.right(angle)
ben.forward(distance)

for _ in range(2):
    ben.right(angle * 2)
    ben.forward(distance)
    ben.right(angle * 2)
    ben.forward(distance)

wn.exitonclick()