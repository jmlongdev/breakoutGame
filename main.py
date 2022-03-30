from turtle import Turtle, Screen
import time
from paddle import Paddle
from score import Score
from ball import Ball

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor('black')
screen.title('Breakout')
# screen.tracer(0)



# places the paddle on the bottom
paddle = Paddle((0, -270))
score = Score()
#allows the paddle to move back and forth
paddle.handle_turtle_drag(0, -270)


screen.mainloop()