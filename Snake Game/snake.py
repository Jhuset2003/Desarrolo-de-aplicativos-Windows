from turtle import Turtle

STARTING_POSITION =[(0,0),(-20,0),(-40,0)]
DISTANCE_MOVE = 10
ARRIBA = 90
ABAJO = 270
IZQUIERDA = 180
DERECHA = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.cabeza = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
    def add_segment(self,position):
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            #self.segments[0].left(105)
            self.cabeza.forward(DISTANCE_MOVE)
    def Up(self):
        if self.cabeza.heading() != ABAJO:
            self.cabeza.setheading(ARRIBA)
    def Down(self):
        if self.cabeza.heading() != ARRIBA:
            self.cabeza.setheading(ABAJO)
    def Left(self):
        if self.cabeza.heading() != DERECHA:
            self.cabeza.setheading(IZQUIERDA)
    def Right(self):
        if self.cabeza.heading() != IZQUIERDA:
            self.cabeza.setheading(DERECHA)