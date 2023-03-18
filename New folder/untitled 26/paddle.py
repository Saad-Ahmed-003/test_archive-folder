from turtle import Turtle

class self(Turtle):
    def __int__(self):
        super().__int__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(350, 0)
