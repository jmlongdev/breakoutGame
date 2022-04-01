from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.lives = 5
        self.score = 0
        self.update_score_and_lives()

    def update_score_and_lives(self):
        self.clear()
        self.goto(380, 205)
        self.write(self.score, align="center", font=("Courier", 75, "normal"))
        self.goto(-380, 205)
        self.write(self.lives, align="center", font=("Courier", 75, "normal"))


    def lives_remaining(self):
        self.lives -= 1
        self.update_score_and_lives()

    def score_point(self):
        self.score += 5
        self.update_score_and_lives()