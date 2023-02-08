from turtle import Screen
from paddle import Paddle
from ball import Ball
from game_board import GameBoard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_one = Paddle(x=-350, y=0)
paddle_two = Paddle(x=350, y=100)

ball = Ball()

board = GameBoard()

screen.listen()
screen.onkeypress(paddle_one.up, "w")
screen.onkeypress(paddle_one.down, "s")
screen.onkeypress(paddle_two.up, "Up")
screen.onkeypress(paddle_two.down, "Down")

game_is_on = True

while game_is_on:
    ball.move()
    screen.update()
    time.sleep(0.02)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bound()

    if paddle_two.distance(ball) < 40 and ball.x > 0:
        ball.rebound()

    if paddle_one.distance(ball) < 40 and ball.x < 0:
        ball.rebound()

    if ball.xcor() > 410:
        board.player_one_win()
        ball.new_ball()

    if ball.xcor() < -410:
        board.player_two_win()
        ball.new_ball()

screen.exitonclick()