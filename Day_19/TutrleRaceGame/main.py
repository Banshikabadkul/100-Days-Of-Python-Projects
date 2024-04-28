from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
#  show a pop up window withtext
user_bet = screen.textinput(title= " Make your bet", prompt= "Which turtle will win the race ?Enter a color: ")
all_turtles = []
colors = ["red", "yellow", "orange","green","blue","purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
for i in range(0,6):
  tim = Turtle(shape="turtle")
  tim.color(colors[i])
  tim.penup()
  tim.goto(x=-230, y=y_pos[i])
  tim.pendown()
  all_turtles.append(tim)
  
if user_bet:
  is_race_on = True

while is_race_on:
  
  for turtle in all_turtles:
    if turtle.xcor() > 230:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"You've won! The {user_bet}")
      else:
        print(f"You''ve lost!! The winning color is {winning_color}")
    rand_dis = random.randint(0,10)
    turtle.penup()
    turtle.forward(rand_dis)

screen.exitonclick()