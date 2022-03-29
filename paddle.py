from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (20, 0), (40, 0)]
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(position)

    def left(self):
        new_x = self.xcor() -20
        self.goto(new_x, self.xcor())

    def right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.xcor())

