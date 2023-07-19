import turtle
turtle.bgcolor("black")
turtle.pensize(5)
turtle.speed(50)


for  i in range(1000):
    for colours in ["red","magenta","blue","cyan","green","yellow","white"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
turtle.hideturtle()