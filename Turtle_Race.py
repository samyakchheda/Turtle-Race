from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(500,500)
user_input=screen.textinput("Make your bet","Which turtle will win the race? Make your bet: ")
color=["Orange","Red","Green","Yellow","Blue","Purple"]
y_axis=[-120,-80,-40,00,40,80]
all_turtle=[]
for i in range(6):
    timm=Turtle("turtle")
    timm.color(color[i])
    timm.penup()
    timm.setposition(-240,y_axis[i])
    all_turtle.append(timm)
is_race_on=False
if user_input:
    is_race_on=True
while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_input:
                print(f"You won the race! {winning_color} turtle is the winner")
            else:
                print(f"You lost the race! {winning_color} turtle is the winner")
        turtle.forward(random.randint(0,10))


screen.exitonclick()
