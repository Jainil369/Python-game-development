import pgzrun
import pygame
WIDTH=400
HEIGHT=400
TITLE="Shapes"


def draw():
    w = 200
    h = 200
    d = 50
    r = 200
    g = 167
    b = 225
    for i in range(10):
        screen.draw.circle((w,h),d,(r,g,b))        
      #rect = Rect(0,0,w,h)
      #rect.center=(200,200)
      #screen.draw.rect(rect, (r,g,b))
        #w -= 10
        #h += 10
        d += 5
        r += 5
        g += 5
        b -= 10
    


pgzrun.go()