from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(500,500)
pen = Turtle()
user_bet = screen.textinput(title="make your bet",prompt="Which turtle will win the race?Enter the color: ")
colors = ["red","green","yellow","orange","blue","purple"]
y_position = [-70,-40,-10,20,50,80]
all_turtles = []
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x = -230, y = y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                pen.penup()  # Don't draw when moving the turtle
                pen.goto(0, 0)  # Move to the center of the screen
                pen.pendown()
                pen.write(f"You've won the race! The {winning_color} turtle is the winner.")
            else:
                pen.penup()  # Don't draw when moving the turtle
                pen.goto(0, 0)  # Move to the center of the screen
                pen.pendown()
                pen.write(f"You lost the race! The {winning_color} turtle is the winner.")

        rand_distance = random.randint(0, 10)

        turtle.forward(rand_distance)




screen.exitonclick()
