from turtle import Turtle, Screen
import time
import random
from paddle import Paddle
from score import Score
from ball import Ball
from block import Brick

screen = Screen()
screen.setup(width=900, height=600)
# screen.setworldcoordinates(0, -12, 12, 24)  # coordinates based on bricks
screen.bgcolor('black')
screen.title('Breakout')
# screen.tracer(0)
COLORS = ['red', 'blue', 'yellow', 'orange', 'green', 'purple']

# places the paddle on the bottom
paddle = Paddle((0, -270))
# allows the paddle to move back and forth
paddle.handle_turtle_drag(0, -270)

# creates the score
score = Score()
# Creates the ball
ball = Ball()
# screen.update()
bricks = Brick()
bricks.create_bricks()
screen.tracer(1)

screen.mainloop()