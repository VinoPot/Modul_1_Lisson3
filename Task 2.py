import turtle as t

screen = t.Screen()
screen.bgcolor("white")
t.speed(5)
t.colormode(255)
t.pensize(2)

for r in range(40, 0, -10):

    for i in range(6):
        t.color(255, 165, r * 6)
        t.fillcolor(162, r * 6, 255)

        t.begin_fill()

        t.circle(r, 360, 3)

        t.end_fill()

        t.rt(60)

t.hideturtle()
screen.exitonclick()