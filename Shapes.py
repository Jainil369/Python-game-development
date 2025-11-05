import pgzrun
WIDTH=400
HEIGHT=400
TITLE="Shapes"


def draw():
    w = 100
    h = 50
    r = 78
    g = 167
    b = 225
    for i in range(10):
      rect = Rect(0,0,w,h)
      rect.center=(200,200)
      screen.draw.rect(rect, (r,g,b))
      w -= 10
      h += 10
      r += 10
      g += 5
      b -= 10
    


pgzrun.go()