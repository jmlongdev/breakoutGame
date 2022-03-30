from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (20, 0), (40, 0)]
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.setpos(position)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.penup()
        self.color("white")
        self.speed(0)
        # self.ondrag(self.goto)

    def handle_turtle_drag(self, x,y):
        self.ondrag(None)
        self.goto(x, -270)
        self.ondrag(self.handle_turtle_drag)


# def handle_turtle_drag(x, y):
#     paddle.ondrag(None)
#     paddle.goto(x, -270)
#     paddle.ondrag(handle_turtle_drag)