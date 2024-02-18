from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("triangle")
        self.penup()
        self.color("white")
        self.setheading(90)
        self.goto(0,-250)
        self.direction="stop"

    def go_right(self):
        self.goto(self.xcor()+20  , self.ycor())

    def go_left(self):
        self.goto(self.xcor()-20  , self.ycor())

