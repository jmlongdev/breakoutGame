from turtle import Turtle
import random

COLORS = ['red', 'blue', 'yellow', 'orange', 'green', 'purple']
CURSOR_SIZE = 20


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.shape('square')
        # self.shapesize(25 / CURSOR_SIZE, 50 / CURSOR_SIZE, 5)
        self.shapesize(2, 4, 1)
        self.hits = 1

    def create_bricks(self):
        for y in range(-100, 250, 20):
            self.setposition(.01 * (y % 2), y + 2.5)
            for x in range(-200, 200, 20):  # baker's dozen due to brick skew
                # self.goto()
                self.color('white', random.choice(COLORS))
                self.stamp()
                self.forward(1)

    # def hit(self):
    #     self.hits -= 1
    #     if self.hits == 0:
    #         self.clearstamp()
