from turtle import Turtle,Screen
from player import Player
from enemy import Enemy



#-----Shooting----#
def shoot():
    if not bullet.isvisible():
        bullet.goto(player.position())
        bullet.showturtle()
def bullet_movement():
    if bullet.isvisible():
        if bullet.ycor() > 275:
            bullet.hideturtle()
        else:
            bullet.forward(bullet_speed)                 

#---------Screen--------#
wn=Screen()
wn.setup(300,300)
wn.title("Space Invaders")
wn.bgcolor("black")
wn.tracer(0)
#--------Player&Enemies-------#
player=Player()
enemy=Enemy()



#--------Bullets------#
bullet = Turtle('triangle', visible=False)
bullet.speed(0)
bullet.color('white')
bullet.shapesize(0.5)
bullet.penup()
bullet.left(90)
bullet_speed = 1

#-------border--------#
border = Turtle(visible=False)
border.speed('fastest')
border.color('green')

border.penup()
border.setposition(-300, -300)
border.pendown()

for _ in range(4):
    border.forward(600)
    border.left(90)

#--------Keybindings------#


should_move = True
wn.listen()
while should_move:
    wn.onkeypress(player.go_left,"a")
    wn.onkeypress(player.go_right,"d")
    if player.xcor() > 250 or player.xcor() < -250:
        should_move = False

wn.onkeypress(shoot,"space")





if __name__ == "__main__":
    while True:
        wn.update()
        enemy.enemy_movement()
        wn.ontimer(bullet_movement,50)
        bullet_movement()
        #------Bullet to obstacle Collision----#
        if bullet.distance(enemy) < 20:
            enemy.hideturtle()
            bullet.hideturtle()


