import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((400,400))
background = pygame.image.load("images/space2.png")
score = 0
font = pygame.font.SysFont("Arial",30)
GameOver = False

class Spaceship(pygame.sprite.Sprite):
    def __init__ (self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.lastshot = pygame.time.get_ticks()
        self.lives = 3
    def move(self):
        global GameOver
        cooldown = 500
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 1
        if key[pygame.K_RIGHT]:
            self.rect.x += 1 
        current_time = pygame.time.get_ticks()   
        if key[pygame.K_SPACE] and current_time - self.lastshot > cooldown:
            bullet1 = Bullet(self.rect.centerx,350)
            bullet_group.add(bullet1)
            self.lastshot = current_time
        if pygame.sprite.spritecollide(self,enemy_group,True):
            self.kill()
            GameOver = True
        d = pygame.sprite.spritecollide(self,enemybullet_group,True)
        for i in d:
           self.lives -= 1
           break
            

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.pos = float(self.rect.y)
        self.velocity = 0
        self.gravity = 0.0001
    def update(self):
        self.velocity += self.gravity
        self.pos += self.velocity
        self.rect.y = int(self.pos)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/laser.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
    def update(self):
        global score
        self.rect.y -= 3
        b =  pygame.sprite.spritecollide(self,enemy_group,True)
        for i in b:
            self.kill()
            score += 1

    
class Enemy_Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/laser2.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
    def update(self):
        self.rect.y += 3


spaceship1 = Spaceship(150,350)

spaceship_group = pygame.sprite.Group()
spaceship_group.add(spaceship1)

enemy_group = pygame.sprite.Group()

bullet_group = pygame.sprite.Group()
enemybullet_group = pygame.sprite.Group()

def enemies():
    for g in range(3):
        for i in range(7):
            enemy2 = Enemy(i * 50 + 50,50*g+50)
            enemy_group.add(enemy2)
   
enemies()

lasts = pygame.time.get_ticks()

while True:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if GameOver == True:
        c = font.render("Game Over",True,"Red")
        screen.blit(c,(200,200))
        pygame.display.update()
        time.sleep(10)
        break
    enemy_group.draw(screen)   
    enemy_group.update()
    bullet_group.draw(screen)
    bullet_group.update()
    spaceship_group.draw(screen)        
    spaceship1.move()
    currentt = pygame.time.get_ticks()
    if currentt - lasts > 1000 and len(enemy_group) > 0:
        en = random.choice(enemy_group.sprites())
        enbullet1 = Enemy_Bullet(en.rect.centerx,en.rect.bottom)
        enemybullet_group.add(enbullet1)  
        lasts = currentt
    enemybullet_group.draw(screen)
    enemybullet_group.update()
    a = font.render("Score:" +str(score),True,"red")
    screen.blit(a,(300,50))
    if spaceship1.lives == 0:
        GameOver = True
    f = font.render("Lives =" +str(spaceship1.lives),True,"blue")
    screen.blit(f,(50,50))
    pygame.display.update()
    
     