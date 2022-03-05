from turtle import Screen
import time
from snake import Snake
from food import Comida


                  
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("First Snake Game AJ")
screen.tracer(0)

serpiente = Snake()
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


    if serpiente.cabeza.distance(comida) < 15:
        comida.refresh()


        

screen.exitonclick()