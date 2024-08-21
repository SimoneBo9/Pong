from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=800,height=600)
my_screen.title("Pong")
my_screen.tracer(0)

paddle_r = Paddle(position=(350,0), wid=5,hei=1)
paddle_l = Paddle(position=(-350,0), wid=5,hei=1)
ball = Ball()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(paddle_r.go_up,"Up")
my_screen.onkey(paddle_r.go_down,"Down")
my_screen.onkey(paddle_l.go_up,"w")
my_screen.onkey(paddle_l.go_down,"s")


game_is_on = True

while game_is_on:
    time.sleep(0.01)
    my_screen.update()
    ball.move()
    if ball.xcor() > 280 or ball.xcor() < -280:
        pass
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()






my_screen.exitonclick()