from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(0, -160)
        self.shape("circle")
        self.color("white")
        self.x_move = 20
        self.y_move = 20
        self.move_speed = .07

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= .9

    def reset_position(self):
        self.goto(0, -160)
        self.bounce_y()