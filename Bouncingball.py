import pgzrun

class Ball():
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius            
        self.color = color
    def draw_ball(self):
        screen.draw.filled_circle((self.x,self.y),self.radius,self.color)


balla = Ball(10,10,40,"red")        

speedy= 0
speedx = 1


def update():
    global speedx
    global speedy
    screen.clear()
 #   if balla.y == 400:
  #      speed = -1
   # elif balla.y == 0:
    #    speed = 1
    if (balla.x,balla.y) == (10,10):
        speedx = 10
        speedy = 0
    if (balla.x,balla.y) == (400,10):
        speedx = 0
        speedy = 10
    if (balla.x,balla.y) == (400,400):
        speedx = -10
        speedy = 0
    if (balla.x,balla.y) == (10,400):
        speedx = 0
        speedy = -10           
    balla.y += speedy
    balla.x += speedx     
    balla.draw_ball()
    

pgzrun.go()        
