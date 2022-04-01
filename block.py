from turtle import Turtle
import random
COLORS = ['red', 'blue', 'yellow', 'orange', 'green', 'purple']
CURSOR_SIZE = 20


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('fast')
        self.shape('square')
        self.shapesize(1, 2)

    def create_bricks(self):
        # self.goto()
        for y in range(-100, 250, 50):
            self.goto(-425, y / 2.4)
            # self.setposition(.01 * (y % 2), y + 2.5)
            for x in range(-200, 220, 20):  # baker's dozen due to brick skew
                # self.goto()
                self.color('white', random.choice(COLORS))
                self.stamp()
                self.forward(40)
                print(self.stamp())

