from turtle import Turtle
import random
COLORS = ['red', 'blue', 'yellow', 'orange', 'green', 'purple']
CURSOR_SIZE = 20

BRICK_COORDS = []
for y in range(-75, 225, 20):
    for x in range(-425, 450, 60):
        brick_coord = (x, y)
        BRICK_COORDS.append(brick_coord)
print(len(BRICK_COORDS))

class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.bricks_list = []
        self.penup()
        # self.shape('square')
        self.shapesize(1, 3)

    def segment(self):
        for i in range(len(BRICK_COORDS)):
            new_brick = Turtle()
            new_brick.penup()
            new_brick.color("white", random.choice(COLORS))
            new_brick.shape("square")
            new_brick.shapesize(stretch_wid=1, stretch_len=3)

            new_brick.goto(BRICK_COORDS[i])
            self.bricks_list.append(new_brick)

    def destroy(self, num):
        for seg in self.bricks_list:
            if seg == self.bricks_list[num]:
                seg.goto(1000, 1000)