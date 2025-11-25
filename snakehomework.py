from turtle import Screen
import pgzrun
import random

WIDTH=500
HEIGHT=500
message="" 
score=0

snake = Actor("snake")
apple = Actor("apple")

def draw(): 
   snake.draw()
   apple.draw()
   screen.draw.text(message,(300,50),fontsize = 15)
   screen.draw.text(str(score),(300,70),fontsize = 15)

def move():
    x = random.randint(0,450)
    y = random.randint(0,450)
    apple.x = (x)
    apple.y = (y)

def update():
    global message
    global score
    if keyboard.left:
        snake.x -= 10
    if keyboard.right:
        snake.x += 10
    if keyboard.up:
        snake.y -= 10
    if keyboard.down:
        snake.y += 10
    if snake.colliderect(apple):
        message = "You have eaten the apple"
        score += 1
        move()
        screen.fill("black")


move()
pgzrun.go()    