import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.penup()
        self.x_move = 1
        self.y_move = 1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()

