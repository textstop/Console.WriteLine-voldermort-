#KEEP UP

import turtle
import os

wn = turtle.Screen()
wn.title("KEEP UP")
wn.bgcolor("black")
wn.setup(width=1000, height= 100)

# Title
print("Try to keep the ball up!")

# Score default setup
score_a = 0

# Bouncer brick
bouncer_a = turtle.Turtle()
bouncer_a.speed(1)
bouncer_a.shape("penatgon")
bouncer_a.color("white")
bouncer_a.shapesize(strentch_wid=1.5, strentch_len=2.3)
bouncer_a.penup()
bouncer_a.goto(-500, 0)

# Invaders
invaders = turtle.Turtle()
invaders.speed(2)
invaders.shape("bot")
invaders.color("grey")
invaders.shapesize(stretch_wid=1, stretch_len=1)
invaders.penup()
invaders.goto(0, 0)
invaders.dx = 2
invaders.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(2)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(-500, 0)
pen.write("The Protector: 0    The Invader: 0")

# Funtions
def invaders_up():
    y = invaders.ycor()
    y += 20
    invaders.sety(y)

def title():
    print("KEEP IT UP!")

def invaders_down():
    y = invaders.ycor()
    y -= 20
    invaders.sety(y)

def bouncer_a_up():
    y = bouncer_a.ycor()
    y += 20
    invaders.sety(y)

def bouncer_down():
    y = bouncer_a.ycor()
    y -= 20
    invaders.sety(y)

# Keyboard movement
wn.listen()
wn.onclick(bouncer_a_up, "i")
wn.onclick(bouncer_down, "k")
wn.onclick(invaders_up, "j")
wn.onclick(invaders_down, "l")

#Main KEEP UP loop
while True:
    wn.update()

    # Move the Invaders
    invaders.setx(invaders.xcor() + invaders.dx)
    invaders.sety(invaders.ycor() + invaders.dy)
    
    # Border Check
    if invaders.ycor() > 490:
        invaders.sety(490)
        invaders.dy *= -1
        os.system("aplay NO!  Sound Effect.mp3&"

    if invaders.xcor() > -510:
        invaders.sety(-510)
        invaders.dy *= -1
        os.system("aplay NO! Sound Effect.mp3&")

# Invader coll
if invaders.xcor() > 490 and invaders.xcor() < 499 and (ball.ycor) + 20 and invaders.ycor() > bouncer_a.ycor()-20):
    invaders.setx(-490)
    invaders.dx *= -1
