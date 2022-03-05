from turtle import Screen
import time
from snake import Snake
from food import Comida
from ScoreBoard import Scoreboard


                  
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("First Snake Game AJ")
screen.tracer(0)

serpiente = Snake()
scoreboard = Scoreboard()
comida = Comida()

screen.listen()
screen.onkey(serpiente.Up, "Up")
screen.onkey(serpiente.Down, "Down")
screen.onkey(serpiente.Left, "Left")
screen.onkey(serpiente.Right, "Right")

 

game_is_ready = True
while game_is_ready:
    screen.update()
    time.sleep(0.1)
    serpiente.move()


    if serpiente.cabeza.distance(comida) < 20:
        comida.refresh()
        scoreboard.increment_score()
        serpiente.extend()

    if serpiente.cabeza.xcor() > 280 or serpiente.cabeza.xcor() < -280 or serpiente.cabeza.ycor() > 280 or serpiente.cabeza.ycor() < -280:
        game_is_ready = False
        scoreboard.game_over()
    for segment in serpiente.segments:
        if segment == serpiente.cabeza:
            pass
        elif serpiente.cabeza.distance(segment) < 10:
            game_is_ready=False
            scoreboard.game_over()

        

screen.exitonclick()