import pygame
import time

pygame.init()
screen = pygame.display.set_mode((400,400))
screen.fill((0,0,0))
pygame.display.update()

class Circle:
    def __init__(self,position,radius,color):
        self.position = position
        self.radius = radius
        self.color = color
        self.window = screen
    def draw(self):
        pygame.draw.circle(self.window,self.color,self.position,self.radius) 
        pygame.display.update()    

red_light = Circle((200,100),50,(255,0,0))        
yellow_light = Circle((200,200),50,(255,255,0))
green_light = Circle((200,300),50,(0,255,0))
red_light.draw()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    time.sleep(3)
    screen.fill("black")
    yellow_light.draw()
    pygame.display.update()
    time.sleep(3)
    screen.fill("black")
    green_light.draw()
    pygame.display.update()
    time.sleep(3)
    screen.fill("black")
    red_light.draw()
    pygame.display.update() 
           