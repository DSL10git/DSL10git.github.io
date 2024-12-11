try:
    from browser import document, alert

    turtle.set_defaults(
        turtle_canvas_wrapper = document["turtle-div"]
    )
except:
    pass

import turtle
import random as r

t = turtle.Turtle()
t.getscreen().bgcolor("black")
t.color("white", "yellow")

def draw_star(turtle_obj, size):
    for side in range(5):
        turtle_obj.forward(size)
        turtle_obj.right(120)
        turtle_obj.forward(size)
        turtle_obj.right(72 - 120)


for _ in range(50):
    x, y = r.randint(-250, 250), r.randint(-250, 250)

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    draw_star(t, r.randint(5, 25))
    t.end_fill()

turtle.done()
