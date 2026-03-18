import pygame 
import random
import math

pygame.init()
screen = pygame.display.set_mode((400,400))
background = pygame.image.load("images/sky2.jpg")
child = pygame.image.load("images/child.png")
apple = pygame.image.load("images/apple.png")
pygame.display.update
x = 150
y = 150
a = random.randint(0,350)
b = random.randint(0,350)
count = 0

def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    

while True:
    screen.blit(background,(0,0))
    screen.blit(child,(x,y))
    screen.blit(apple,(a,b))    
    count += 1
    if count % 600 == 0: 
        a = random.randint(0, 350)
        b = random.randint(0, 350)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 30
            if event.key == pygame.K_RIGHT:
                x += 30
            if event.key == pygame.K_UP:
                y -= 30 
            if event.key == pygame.K_DOWN:
                y += 30
    if distance(x,y,a,b) < 50:
        break
    pygame.display.update()