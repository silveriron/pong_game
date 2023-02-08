from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.speed(0)
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.setpos(x=x, y=y)

    def up(self):
        self.sety(self.ycor()+20)

    def down(self):
        self.sety(self.ycor()-20)