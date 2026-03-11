import pygame
import random

pygame.init()
screen = pygame.display.set_mode((300,300))
screen.fill((255,215,0))
pygame.display.update()

class Circle():
    def __init__(self,position,radius,color):
        self.position = position
        self.radius = radius            
        self.color = color
        self.window = screen
    def draw(self):
        pygame.draw.circle(self.window,self.color,self.position,self.radius) 
    def increase(self):
        self.radius += 10    
        self.draw()
    def decrease(self):
        self.radius -= 10
        self.draw()    
    def colour_change(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.color = (r,g,b)
        self.draw()     

class Square():
    def __init__(self,position,size,color):
        self.position = position
        self.size = size            
        self.color = color
        self.window = screen
    def draw(self):
        pygame.draw.rect(self.window,self.color,(self.position,self.size))    
    def increase(self):
        self.size = (self.size[0]+10,self.size[1]+10)
        self.draw()
    def decrease(self):
        self.size = (self.size[0]-10,self.size[1]-10)
        self.draw()    



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            circle1.position = event.pos
            circle1.draw()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                circle1 = Circle((150,150),25,"orange")
            if event.key == pygame.K_DOWN:
                circle1.increase()
            if event.key == pygame.K_UP:
                circle1.colour_change()     
            if event.key == pygame.K_RIGHT:
                circle1.decrease()       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                square1 = Square((150,150),(50,50),"blue")
                square1.draw()
            if event.key == pygame.K_s:
                square1.increase()
            if event.key == pygame.K_d:
                square1.decrease()    
                             
    pygame.display.update()    

