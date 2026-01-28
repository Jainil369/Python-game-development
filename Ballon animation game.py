import pgzrun
import random

WIDTH = 500
HEIGHT = 450

balloon = Actor('balloon')
child = Actor('child')
balloon.y = 400
child.y = 400

def draw():
    screen.blit("sky2", (0, 0))
    balloon.draw()
    child.draw()


def animate_balloon():
    animate(balloon,y = 10,angle = 360,x = 150,duration = 4 )

animate_balloon()    



pgzrun.go()