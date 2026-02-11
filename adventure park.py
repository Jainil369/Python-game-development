import pgzrun
import random
import math 

WIDTH = 600
HEIGHT = 400
child = Actor('child',(50,350))
ferriswheel = Actor("ferris wheel")

def draw():
    screen.blit("sky2", (0, 0))
    child.draw()
    ferriswheel.draw()

def ferriswheel_animation():
    angle = 0
    animate(ferriswheel, angle = ferriswheel.angle + 10, duration = 1, on_finished = ferriswheel_animation)



def child_animationright():
    animate(child, pos = (350,350),duration = 5, on_finished = child_animationleft)

def child_animationleft():
    animate(child, pos = (50,350),duration = 5, on_finished = child_animationright)    




child_animationright()
ferriswheel_animation() 
pgzrun.go()