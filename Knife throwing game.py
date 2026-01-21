import pgzrun
import random
from pgzero import actor, screen, keyboard

HEIGHT=400
WIDTH=500

knife = Actor("knife")
apple = Actor("apple")
apple.x = random.randint(0,450)
apple.y = 100
knife.y = 340
knife.x = 220
knifethrow = False
speed = 1.5
score = 0

def draw():
    screen.blit("sky2",(0,0))
    screen.draw.text(str(score),(470,50),fontsize = 30)
    knife.draw()
    apple.draw()

def apples():
    pass    
        

def update():
    global knifethrow
    global score
    if keyboard.left and knifethrow == False:
        knife.x -= 10
    if keyboard.right and knifethrow == False:
        knife.x += 10        
    if keyboard.space:
        knifethrow = True
    if knifethrow == True:
        knife.y -= 5
    if knife.colliderect(apple):
        knife.y = 340
        knife.x = 220
        knifethrow = False
        score += 1
    if knife.y <= 0:
        knife.y = 340
        knife.x = 220
        knifethrow = False



pgzrun.go()