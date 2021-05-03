from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Whci turtle will win the game? Pick a color:")
colors=["red","orange","yellow","green","blue","purple"]
y_pos=[-70,-40,-10,20,50,80]
all_turtle=[]
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtle.append(new_turtle)
if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            winning_color=turtle.pencolor()
            is_race_on=False
            if winning_color==user_bet:
                print(f"You have won! The {winning_color} turtle is the winner")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner")
            
        rand_dist=random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()
