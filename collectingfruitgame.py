import pgzrun
import random

HEIGHT=500
WIDTH=500

basket = Actor("basket")
apple = Actor("apple")
banana = Actor("banana")
basket.y = (450)
banana.x = random.randint(0,450)
apple.x = random.randint(0, 450)
fruits = [apple,banana]
score = 0
bombs = []

def draw():
    screen.clear()
    screen.blit("sky",(0,0))
    basket.draw()
    apple.draw()
    banana.draw()
    for bomb in bombs:
        bomb.draw()
    screen.draw.text(str(score),(300,70),fontsize = 15)

def bombss():
    bomb = Actor("bomb")
    bomb.x = random.randint(0,450)
    bombs.append(bomb)
    clock.schedule(bombss,10)

def update():
    global score
    if keyboard.left:
        basket.x -= 10
    if keyboard.right:
        basket.x += 10
    for fruit in fruits:
        fruit.y += 2    
        if fruit.colliderect(basket):
            fruit.x = random.randint(0,450)
            fruit.y = 0
            score += 1
        if fruit.y > 450:
            fruit.x = random.randint(0,450)
            fruit.y = 0
    for bomb in bombs:
        bomb.y += 2
        if bomb.colliderect(basket):
            score -= 4    
            bombs.remove(bomb)

            
clock.schedule(bombss,10)

pgzrun.go()
