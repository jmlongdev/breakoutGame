from turtle import Turtle, Screen
import time
import random
from paddle import Paddle
from score import Score
from ball import Ball
from block import Brick
from lives import Lives

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)
COLORS = ['red', 'blue', 'yellow', 'orange', 'green', 'purple']

paddle = Paddle((0, -270))
screen.listen()
paddle.handle_turtle_drag(0, -270)

lives = Lives()
score = Score()
ball = Ball()
bricks = Brick()
bricks.create_bricks()


screen.listen()
screen.onkeypress(paddle.l_move, "Left")
screen.onkeypress(paddle.r_move, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.xcor() > 430 or ball.xcor() < -430:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.ycor() < -280:
        ball.reset_position()
        lives.lives_remaining()

    if lives.lives == 0:
        print('Game Over')
        game_is_on = False

    if ball.distance(paddle) < 60 and ball.ycor() > -270:
        ball.bounce_y()

    if abs(ball.xcor() - bricks.xcor()) < 20 and bricks.ycor() <= ball.ycor() <= bricks.ycor() + 10:
        print("colided with the brick:")



screen.mainloop()

