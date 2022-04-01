from turtle import Turtle, Screen
import time
import random
from paddle import Paddle
from score import Score
from ball import Ball
from brick import Bricks
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
brick = Bricks()
# brick.create_bricks()
brick.segment()
screen.listen()
screen.onkeypress(paddle.l_move, "Left")
screen.onkeypress(paddle.r_move, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    for i in range(len(brick.bricks_list)):
        if ball.distance(brick.bricks_list[i]) < 40:
            ball.bounce_y()
            brick.destroy(i)
            score.score_point()

    if ball.xcor() > 430 or ball.xcor() < -430:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.ycor() < -280:
        ball.bounce_y()
        ball.reset_position()
        # lives.lives_remaining()

    if lives.lives == 0:
        print('Game Over')
        game_is_on = False
    else:
        if score.score > 1125:
            game_is_on = False
            print("You win!")

    if ball.distance(paddle) < 60 and ball.ycor() > -270:
        ball.bounce_y()

screen.mainloop()

