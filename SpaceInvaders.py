import pygame

pygame.init()
screen = pygame.display.set_mode((400,400))
background = pygame.image.load("images/space2.png")

class Spaceship(pygame.sprite.Sprite):
    def __init__ (self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 1
        if key[pygame.K_RIGHT]:
            self.rect.x += 1    

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/laser.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
    def update(self):
        self.rect.y -= 3





spaceship1 = Spaceship(150,350)

spaceship_group = pygame.sprite.Group()
spaceship_group.add(spaceship1)


bullet_group = pygame.sprite.Group()

while True:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.K_SPACE:
            bullet1 = Bullet(spaceship1.rect.x,350)
            bullet_group.add(bullet1)
    bullet_group.draw(screen)
    bullet_group.update()
    spaceship_group.draw(screen)        
    spaceship1.move()
    pygame.display.update()
    
    