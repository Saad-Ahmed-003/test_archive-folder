from turtle import Turtle


class Paddle(Turtle):
    def __int__(self, position):
        super().__init__()
        paddle = Turtle()
        paddle.shape("square")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.color("White")
        paddle.penup()
        paddle.goto(position)

    def go_up(self):
        new_y = self.ycor() + 28
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 28
        self.goto(self.xcor(), new_y)
