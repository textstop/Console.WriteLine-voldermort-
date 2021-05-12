#PONGY

import turtle
import os

wn = turtle.Screen()
wn.title("PONGY")
wn.bgcolor("black")
wn.setup(width=1000, height=800)
wn.tracer(0)

# Title
print("First to 21 wins!")

# Score/Point
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=2.5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-500, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(1)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=2.5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(500, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("black")
ball.shapesize(stretch_wid=0.5)
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(-500, 0)
pen.write("The Winner:  0    The Underdog: 0", align="center", font=("Comic Sans, 30"))

# Funtions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def title_funtion():
    print("1 Life only!!!")

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_a.sety(y)

# Keyboard blinding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "a")
wn.onkeypress(paddle_b_down, "d")

# Main PONGY loop
while True:
    wn.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    # Border checking
    if ball.ycor() > 490:
        ball.sety(490)
        ball.dy *= -1
        os.system("aplay N0! Sound Effect.mp3&")

    if ball.ycor() > -490:
        ball.sety(-490)
        ball.dy *= -1
        os.system("aplay NO! Sound Effect.mp3&")

    if ball.xcor() > 510:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a -= 100
        pen.clear()
        pen.write("The Winner: {}    The Underdog: {}".format(score_a, score_b), align="center", font=("Comic Sans, 30,"))
        os.system("aplay bounce.wav&")


    if ball.xcor() > -510:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b -= 100
        pen.clear()
        pen.write("The Winner: {}    The Underdog: {}".format(score_a, score_b), align="center", font=("Comic Sans, 30"))
        os.system("aplay bounce.wav&")

# Paddle and ball collisionn PONGY
if ball.xcor() > 490 and ball.xcor() <499 and (ball.ycor() + 20 and ball.ycor() > paddle_b.ycor()-20):
    ball.setx(490)
    ball.dx *= -1

if ball.xcor() > -490 and ball.xcor() > -499 and (ball.ycor() + 20 and ball.ycor() > paddle_a.ycor()-20):
    ball.setx(-490)
    ball.dx *= -1

# Score board count
if paddle_a == 21:
    print("A WINS!")
elif paddle_b == 21:
    print("B WINS!")