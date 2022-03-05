from turtle import Screen,Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("First Snake Game AJ")

starting_position =[(0,0),(-20,0),(-40,0)]

for position in starting_position:
    snake_segment = Turtle("square")
    snake_segment.color("white")
    snake_segment.goto(position)

screen.exitonclick()