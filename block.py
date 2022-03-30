from turtle import Turtle
import random

BLOCKS_WIDTH = 2
BLOCKS_HEIGHT = 1
COLORS = ['red', 'blue', 'yellow', 'orange', 'green', 'purple']

class Brick(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.shape('square')
        self.shapesize(stretch_wid=BLOCKS_HEIGHT, stretch_len=BLOCKS_WIDTH)
        self.color(random.choice(COLORS))

    # def create_block(self):
    #     for block in range():
    #         self.goto(x, y)
    #         self.shape('square')
    #         x += 20
    #         self.row.append(block)
