import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(45)
        self.x = 5
        self.y = 5

    def move(self):
        self.goto(x=self.xcor()+self.x, y=self.ycor()+self.y)

    def bound(self):
        self.y *= -1

    def rebound(self):
        self.x *= -1

    def new_ball(self):
        self.goto(x=0, y=0)