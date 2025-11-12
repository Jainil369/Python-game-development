from turtle import Screen
import pgzrun
import random

WIDTH=500
HEIGHT=500

Alien=Actor("alien")
message = ""

def draw():
    Alien.draw()
    screen.draw.text(message,(300,50),fontsize = 15)
    screen.draw.text(str(score),(250,50),fontsize = 15)
    
def move():
    x = random.randint(0,450)
    y = random.randint(0,450)
    Alien.x=(x)
    Alien.y=(y)

score=0

def on_mouse_down(pos):
    global message
    global score
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    if Alien.collidepoint(pos):
        message = "Good shot"
        move()
        score+=1
        screen.fill((r,g,b))
    else:
        screen.fill("black")
        message = "Unlucky"  

move()    

pgzrun.go()