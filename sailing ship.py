import pgzrun
import random

WIDTH = 550
HEIGHT = 270 
ship = Actor("ship")
ship.x = 50
ship.y = 150   

def draw():
    screen.blit("waves", (-20,0))
    ship.draw()

def animate_shipup():
    animate(ship, x = ship.x + 50,angle = 20, duration = 2, on_finished = animate_shipdown)

def animate_shipdown():
    animate(ship, x = ship.x + 50,angle = -20, duration = 2, on_finished = animate_shipup)

animate_shipup()   


pgzrun.go()