from turtle import Turtle

ALIGN = "center"
FONT = ("roboto", 24, "normal")

class GameBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = [0, 0]
        self.ht
        self.penup()
        self.sety(250)
        self.right(90)
        self.color("white")
        self.show_score()
        self.draw_line()
        self.ht()

    def show_score(self):
        self.write(f"{self.score[0]} : {self.score[1]}", align=ALIGN, font=FONT)

    def draw_line(self):
        while self.ycor() > -270:
            self.forward(20)
            self.pendown()
            self.forward(20)
            self.penup()

        self.sety(250)

    def player_one_win(self):
        self.score[0] += 1
        self.clear()
        self.show_score()
        self.draw_line()

    def player_two_win(self):
        self.score[1] += 1
        self.clear()
        self.show_score()
        self.draw_line()