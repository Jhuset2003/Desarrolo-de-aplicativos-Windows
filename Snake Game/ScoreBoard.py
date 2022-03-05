from turtle import Turtle

TITLE_SCORE = ("Arial",30,"bold")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.goto(0,250)
        self.clear()
        self.color("blue")
        self.update_score()
        self.hideturtle()
        self.penup()
    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=TITLE_SCORE )
    def increment_score(self):
        self.clear()
        self.score += 1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Arial",40,"bold"))