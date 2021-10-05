from typing import Text
from settings import initChallenges
from collision import checkChallengesCollision
from Colors import *
from settings import *

'''
0 = Terrain
1 = Caillasse
2 = L'eau
3 = Foret
4 = Sable
5 = Defi
'''

format_prefix = "\033["
position_suffix = "H"

ul = "╔"
ur = "╗"
bl = "╚"
br = "╝"
c = "║"
r = "═"
cl = "╣"
cr = "╠"

map_height = 30
map_width = 50
map_margin = 4
def printAt(x, y, text):
    print(f"{format_prefix}{y};{x}{position_suffix}{text}")

def printBoard():
    range_y = map_height+map_margin+1
    range_x = map_width+ map_margin*2
    for y in range(range_y):
        for x in range(range_x):
            if y == 0 and x == 0:
                printAt(x,y,ul)
            elif y == 0 and x == range_x-1:
                printAt(x,y,ur)
            elif y == 0 and x >1:
                printAt(x,y,r)
            elif y == 3 and x == 0:
                printAt(x,y,cr)
            elif y == 3 and x == range_x-1:
                printAt(x,y,cl)
            elif y == 3 and x > 1:
                printAt(x,y,r)
            elif x == 0 and y >1:
                printAt(x,y,c)
            elif y == range_y-1 and x == 1:
                printAt(x,y,bl)
            elif y == range_y -1 and x>1 and x < range_x-1:
                printAt(x,y,r)
            elif y == range_y-1 and x == range_x-1:
                printAt(x,y,br)
            elif x == range_x-1 and y >1:
                printAt(x,y,c)

def printMap():
    printBoard()
    challenges = initChallenges()
    for y in range(len(map_mattrix)):
        for x in range(len(map_mattrix[y])):
            map_elem = map_mattrix[y][x]
            style = ""
            txt = " "
            # Challenges
            if checkChallengesCollision(challenges, x, y):
                style = TextColors.RED
                txt = "X"
            # Pierre
            elif map_elem == 1:
                # back_color = BackgroundColors.WHITE
                txt = "▲"
            # Mer
            elif map_elem == 2:
                style = TextColors.BLUE
                txt = "░"
            # Arbre
            elif map_elem == 3:
                style = TextColors.GREEN
                txt = "░"
            # Arbre 2
            elif map_elem == 4:
                style = TextColors.GREEN
                txt = "♣"
            # Sable
            elif map_elem == 5:
                style = TextColors.YELLOW
                txt = "░"
            # Joueur
            if x == p.POS_X and y == p.POS_Y:
                style += TextColors.WHITE
                txt = "a"
            printAt(x+map_margin , y+map_margin , f'{style}{txt}{TextColors.RESET_ALL}')
    # print('Haut: "z", Gauche: "q", Bas: "s", Droite:"d" | Inventaire: "e" | Quitter: "l"')
    printAt(map_width//2-len(p.NAME),2, f"Partie de {p.NAME} !")
    printAt(map_width//2//2, map_height+5,f'Position Y: {p.POS_Y} | Position X: {p.POS_X}')
