import pgzrun
import random

HEIGHT=400
WIDTH=500

mine = Actor("spaceship")
mine.x = 100
mine.y = 360
enemys = []


def draw():
    screen.blit("space2",(0,0))
    mine.draw()
    for enemy in enemys:
        enemy.draw()

def enemies():
    for i in range(3):
        enemys.append(Actor("enemy"))
        enemys[-1].x = random.randint(0,450)
        enemys[-1].y = 25







def update():
    if keyboard.left:
        mine.x -= 10
    if keyboard.right:
        mine.x += 10    








enemies()
pgzrun.go()  



