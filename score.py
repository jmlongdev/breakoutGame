from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(370, 205)
        self.write(self.score, align="center", font=("Courier", 75, "normal"))

    def score_point(self):
        self.score += 5
        self.update_score()