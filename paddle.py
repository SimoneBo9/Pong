from turtle import Turtle


MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position, wid, hei):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=wid, stretch_len=hei)
        self.penup()
        self.goto(position)


    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_left (self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())