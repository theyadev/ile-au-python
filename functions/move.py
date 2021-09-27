import settings
from collision import collision
from map import printMap
from clear import clear

def move(x, y, p):
    if collision(x, y, p) == False:
        p["pos"]["x"] += x
        p["pos"]["y"] += y
        pos = settings.M[p["pos"]["y"]][p["pos"]["x"]]
        if (pos == 5):
            clear()
            print('DEFI !!!!!!!!!!!')
        else:
            printMap(p)