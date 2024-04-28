from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
  tim.forward(10)
  
def move_backward():
  tim.backward(10)

def turn_left():
  # left turn upwards
  new_heading = tim.heading() + 10
  tim.setheading(new_heading)

def turn_right():
  new_heading = tim.heading() - 10
  tim.setheading(new_heading)
  
def clear_screen():
  tim.clear()
  tim.penup()
  tim.home()
  tim.pendown()

screen.listen()
screen.onkey(key="W", fun=move_forward)
screen.onkey(key="S", fun=move_backward)
screen.onkey(key="A", fun=turn_left)
screen.onkey(key="D", fun=turn_right)
screen.onkey(key="C", fun=clear_screen)

screen.exitonclick()