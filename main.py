from turtle import Turtle, Screen
import time
from paddle import Paddle
from score import Score
from ball import Ball
import random
from block import Brick
screen = Screen()
screen.setup(width=900, height=600)
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

# row_1 = BlockRow(0,0)
# row_1.create_block()

bricks = []
for y in range(25, 200, 25):
    color = random.choice(COLORS)
    for x in range(-420, 425, 50):
        bricks.append(Brick(x, y))
        # bricks[-1].color = color


screen.mainloop()