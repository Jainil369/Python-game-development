from turtle import Screen
import pgzrun
import random

WIDTH=500
HEIGHT=400
message = ""
score = 0

Bumblebee = Actor("bumblebee")
flower = Actor("flower")

def draw():
    screen.blit("space",(0,0))
    Bumblebee.draw()
    flower.draw()
    Screen.draw.text(message,(300,50),fontsize = 15)
    Screen.draw.text(str(score),(300,70),fontsize = 15)

def move():
    x = random.randint(0,450)
    y = random.randint(0,450)
    flower.x = (x)    
    flower.y = (y)

def update():
    global message
    global score
    if keyboard.left:
        Bumblebee.x -= 10
    if keyboard.right:
        Bumblebee.x += 10
    if keyboard.up:
        Bumblebee.y -= 10
    if keyboard.down:
        Bumblebee.y += 10
    if Bumblebee.colliderect(flower):
        message = "You have caught the flower"
        score += 1
        move()


                 







    











move()
pgzrun.go()