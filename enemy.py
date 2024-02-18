from turtle import Turtle

class Enemy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.speed("fast")
        self.setpos(-250 , 250)
        self.speed= 1
        self.direction = 1
    def enemy_movement(self):
        self.forward(self.direction * self.speed)
        self.settiltangle(self.tiltangle() + 3)
        self.x,self.y = self.position()

        if self.x > 250 or self.x < -250:
            self.direction *= -1
            self.sety(self.y-25)
    

