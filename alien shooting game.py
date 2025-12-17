import pgzrun
import random

HEIGHT=400
WIDTH=500

mine = Actor("spaceship")
boss = Actor("bossenemy")
boss.x = 250
mine.x = 100
mine.y = 360
enemys = []
gameover = False
lasers = []
alasers = []
live = 3
score = 0
message = "Score = "
z = 20
e = False
h = 100

def draw():
    screen.draw.text(str(score),(470,50),fontsize = 30)
    screen.draw.text(message,(400,50),fontsize = 30)    
    screen.draw.text(str(live),(25,50),fontsize = 30) 
    screen.draw.text(str(h),(25,70),fontsize = 30) 
    if gameover:
        return
    screen.blit("space2",(0,0))
    mine.draw()
    if e == True:
        boss.draw()
    for laser2 in alasers:
        laser2.draw()
    for laser in lasers:
        laser.draw()
    for enemy in enemys:
        enemy.draw()

def enemies():
    if e == False:
        for i in range(7):
            global z
            enemys.append(Actor("enemy"))
            enemys[-1].x = z
            z += 45
            if z > 450:
                z = 20
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
    global live
    global score
    global e
    global h
    global message
    if gameover:
        return
    if live == 0:
        gameover = True
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
                score += 1
        if laser.colliderect(boss) and e == True:
                h -= 5      
                lasers.remove(laser)
        if h == 0:
            message = "You have won the game"
            gameover = True
    for laser2 in alasers:
        laser2.y += 2
        if laser2.colliderect(mine):
            live -= 1
            alasers.remove(laser2)
    if score > 25:
        e = True
        boss.y += 0.1

    
enemies()
alienlaser()
pgzrun.go()  



