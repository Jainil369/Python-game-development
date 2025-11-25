import pgzrun
import random

HEIGHT=500
WIDTH=500

star = Actor("star1")
star1 = Actor("star1")
star.x = random.randint(0,200)
star1.x = random.randint(0,200)

st = [star,star1]
 
def draw():
    screen.clear()
    screen.blit("space2",(0,0))
    for star in st: 
        star.draw()

def update():
        for star in st:
            star.x = star.x + 2
            star.y = star.y + 2
            if star.x > 450:
                star.x = random.randint(0,200)
                star.y = 0    

pgzrun.go()