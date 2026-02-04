import pgzrun
import random 
import math

WIDTH = 650
HEIGHT = 400    

sun = Actor('sun', (325,200))
mercury = Actor('mercury')
venus = Actor('venus')
earth = Actor('earth')
mars = Actor('mars')
jupiter = Actor('jupiter' )
mring = Actor('mring', sun.pos)
vring = Actor('vring', sun.pos)
ering = Actor('ering', sun.pos)
m2ring = Actor('m2ring', sun.pos)
jring = Actor('jring', sun.pos)

def draw():
    screen.blit("space2",(0,0))
    sun.draw()
    mring.draw()
    vring.draw()    
    ering.draw()
    m2ring.draw()
    jring.draw()
    venus.draw()
    mercury.draw()
    earth.draw()
    mars.draw()
    jupiter.draw()


mangle = 0

def animate_mercury():
    global mangle
    x = sun.x + 50 * math.cos(mangle)
    y = sun.y + 50 * math.sin(mangle)
    mangle = mangle + 0.3
    animate(mercury,pos = (x,y), duration = 0.5, on_finished = animate_mercury)   

vangle = 0   

def animate_venus():
    global vangle
    x = sun.x + 80 * math.cos(vangle)
    y = sun.y + 80 * math.sin(vangle)
    vangle = vangle + 0.3
    animate(venus,pos = (x,y), duration = 0.6, on_finished = animate_venus)

eangle = 0

def animate_earth():
    global eangle
    x = sun.x + 110 * math.cos(eangle)
    y = sun.y + 110 * math.sin(eangle)
    eangle = eangle + 0.3    
    animate(earth,pos = (x,y), duration = 0.7, on_finished = animate_earth)  

m2angle = 0

def animate_mars():
    global m2angle
    x = sun.x + 140 * math.cos(m2angle)
    y = sun.y + 140 * math.sin(m2angle)
    m2angle = m2angle + 0.3    
    animate(mars, pos = (x,y), duration = 0.8, on_finished = animate_mars)      

jangle = 0

def animate_jupiter():
    global jangle
    x = sun.x + 180 * math.cos(jangle)
    y = sun.y + 180 * math.sin(jangle)
    jangle = jangle + 0.3   
    animate(jupiter, pos = (x,y), duration = 0.9, on_finished = animate_jupiter)



animate_mercury()
animate_venus()
animate_earth()
animate_mars()
animate_jupiter()
pgzrun.go()    