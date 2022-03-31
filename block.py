from turtle import Turtle
import random
#
# BLOCKS_WIDTH = 2
# BLOCKS_HEIGHT = 1
COLORS = ['red', 'blue', 'yellow', 'orange', 'green', 'purple']
#
#
# class Brick(Turtle):
#     def __init__(self, x, y):
#         super().__init__()
#         self.penup()
#         self.goto(x, y)
#         self.shape('square')
#         self.shapesize(stretch_wid=BLOCKS_HEIGHT, stretch_len=BLOCKS_WIDTH)
#         self.color(random.choice(COLORS))
#         self.speed('fastest')
#         self.bricks = []
#
#     def create_bricks(self):
#         for y in range(25, 200, 25):
#             # self.color(random.choice(COLORS))
#             for x in range(-420, 425, 50):
#                 self.goto(x,y)
#                 self.bricks.append(Brick(x, y))

    # def create_block(self):
    #     for block in range():
    #         self.goto(x, y)
    #         self.shape('square')
    #         x += 20
    #         self.row.append(block)

CURSOR_SIZE = 20


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.shapesize(25 / CURSOR_SIZE, 50 / CURSOR_SIZE, 5)

    def create_bricks(self):
        for y in range(24):
            self.setposition(-0.5 * (y % 2), y + 0.3)
            for x in range(13):  # baker's dozen due to brick skew
                self.color('black', random.choice(COLORS))
                self.stamp()
                self.forward(1)
