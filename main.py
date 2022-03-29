from turtle import Turtle, Screen
import time
from paddle import Paddle
# from score import Score
from ball import Ball

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor('black')
screen.title('Breakout')
# screen.tracer(0)

# paddle = Paddle((0, 20))
#
# paddle.ondrag(paddle.goto)


def handle_turtle_drag(x,y):
    t.ondrag(None)
    t.goto(x, y)
    t.ondrag(handle_turtle_drag)

t = Turtle(shape='circle')
t.color('white')
t.speed(0)
t.ondrag(handle_turtle_drag)

screen.mainloop()