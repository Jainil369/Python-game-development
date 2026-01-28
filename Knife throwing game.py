import pgzrun
import random

HEIGHT=400
WIDTH=500

knife = Actor("knife")
apple = Actor("apple")
apple.x = random.randint(0,450)
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

def distance(knife,apple):
    return ((knife.x - apple.x)**2 + (knife.y - apple.y)**2)**0.5

   

def move():
    global speed
    apple.x += speed
    if apple.x <= 10:
        speed = 1.5
    if apple.x >= 450:
        speed = -1.5    
        

def update():
    global knifethrow
    global score
    global speed
    move()
    if score > 5:  
       if apple.x <= 10:
        speed = 5
       if apple.x >= 450:
        speed = -5 
    if score > 10:  
       if apple.x <= 10:
        speed = 10
       if apple.x >= 450:
        speed = -10   
    if keyboard.left and knifethrow == False:
        knife.x -= 10
    if keyboard.right and knifethrow == False:
        knife.x += 10        
    if keyboard.space:
        knifethrow = True
    if knifethrow == True:
        knife.y -= 5
    if distance(knife,apple) < 30:
        knife.y = 340
        knife.x = 220
        knifethrow = False
        score += 1
    if knife.y <= 0:
        knife.y = 340
        knife.x = 220
        knifethrow = False



pgzrun.go()