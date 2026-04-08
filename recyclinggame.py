import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400,400))
background = pygame.image.load("images/shadedbackground.jfif")
images = ["images/box.png","images/Clothes.png"]


class Recyclable(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

class NonRecyclables(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bottle.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

class Bin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/recyclingbin.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

recyclable_group = pygame.sprite.Group()
nonrecyclable_group = pygame.sprite.Group()

for i in range(20):
    recyclable = Recyclable(random.choice(images),random.randint(0,350),random.randint(0,350))
    recyclable_group.add(recyclable)

for i in range(10):
    nonrecyclable = NonRecyclables(random.randint(0,350),random.randint(0,350))
    nonrecyclable_group.add(nonrecyclable)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    recyclable_group.draw(screen)
    nonrecyclable_group.draw(screen)
    pygame.display.update()