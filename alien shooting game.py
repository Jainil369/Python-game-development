import pgzrun
import random

HEIGHT=400
WIDTH=500

mine = Actor("spaceship")
mine.x = 100
mine.y = 360
enemys = []
gameover = False
message = ""
lasers = []
alasers = []


def draw():
    if gameover:
        return
    screen.blit("space2",(0,0))
    mine.draw()
    for laser2 in alasers:
        laser2.draw()
    for laser in lasers:
        laser.draw()
    for enemy in enemys:
        enemy.draw()
    screen.draw.text(message,(300,50),fontsize = 15)    

def enemies():
    for i in range(7):
        enemys.append(Actor("enemy"))
        enemys[-1].x = random.randint(0,450)
        enemys[-1].y = 25
    clock.schedule(enemies,5)    

def alienlaser():
    alasers.append(Actor("laser2"))
    one = random.choice(enemys)
    alasers[-1].x = one.x
    alasers[-1].y = one.y
    clock.schedule(alienlaser,1)   


def on_key_down(key):
    if key == keys.SPACE:
        laser = Actor("laser")
        lasers.append(laser)
        laser.x = mine.x
        laser.y = mine.y

def update():
    global gameover
    if gameover:
        return
    if keyboard.left:
        mine.x -= 10
    if keyboard.right:
        mine.x += 10    
    for enemy in enemys:
        enemy.y += 0.5
        if enemy.y > 400:
            enemys.remove(enemy)
        if enemy.colliderect(mine):
            gameover = True
    for laser in lasers:
        laser.y -= 3
        for enemy in enemys:
            if laser.colliderect(enemy):
                enemys.remove(enemy)        
    for laser2 in alasers:
        laser2.y += 2
                    
            
    
enemies()
alienlaser()
pgzrun.go()  



