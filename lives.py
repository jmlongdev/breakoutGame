from turtle import Turtle


class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.lives = 5
        self.update_lives()

    def update_lives(self):
        self.clear()
        self.goto(-380, 205)
        self.write(self.lives, align="center", font=("Courier", 75, "normal"))

    def lives_remaining(self):
        self.lives -= 1
        self.update_lives()
