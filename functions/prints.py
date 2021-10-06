from time import sleep
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

up_left = "╔"
up_right = "╗"
bot_left = "╚"
bot_right = "╝"
vertical = "║"
horizontal = "═"
vert_left = "╣"
vert_right = "╠"
horizontal_bot = "╦"
cross ="╬"

board_size = 100

map_height = 30
map_width = 50
map_margin = 4

range_y = map_height+map_margin+1
range_x = map_width+ map_margin*2

food_stam_size = 9
pos_water_y = 7
pos_stamina_y = 5
pos_food_y = 3

def printAt(x, y, text):
    print(f"{format_prefix}{y};{x}{position_suffix}{text}")

def printBoard():
    for y in range(range_y):
        for x in range(board_size):
            if x == 0 or x == range_x-1:
                if y >1:
                    printAt(x,y,vertical)
            if x == board_size-1:
                if 1<y<food_stam_size:
                    printAt(x,y,vertical)
            if y == 0:
                if x == 0:
                    printAt(x,y,up_left)
                elif x == range_x-1:
                    printAt(x,y,horizontal_bot)
                elif x == board_size-1:
                    printAt(x,y, up_right)
                elif x > 1:
                    printAt(x,y,horizontal)
            elif y == 3:
                if x == 0:
                    printAt(x,y,vert_right)
                elif x == range_x-1:
                    printAt(x,y,vert_left)
                elif x > 1 and x < range_x:
                    printAt(x,y,horizontal)
            elif y == food_stam_size:
                if x == range_x-1:
                    printAt(x,y, vert_right)
                elif x == board_size-1:
                    printAt(x,y,bot_right)
                elif x >= range_x:
                    printAt(x,y,horizontal)
                elif x == 0: printAt(x,y,vertical)
            elif y == range_y-1:
                if x == 1:
                    printAt(x,y,bot_left)
                elif x>1 and x < range_x-1:
                    printAt(x,y,horizontal)
                elif x == range_x-1:
                    printAt(x,y,bot_right)


def printFoodAndStamina():
    printAt(range_x+1, pos_food_y, f"Nourriture: {BackgroundColors.RED}{' '*(int(round(p.FOOD/5)))}{BackgroundColors.RESET}{' '*(20-int(round(p.FOOD/5)))}")
    printAt(range_x+1, pos_stamina_y, f"Energie: {BackgroundColors.YELLOW}{' '*(int(round(p.STAMINA/5)))}{BackgroundColors.RESET}{' '*(20 - int(round(p.STAMINA/5)))}")
    printAt(range_x+1, pos_water_y, f"Soif: {BackgroundColors.CYAN}{' '*(int(round(p.WATER/5)))}{BackgroundColors.RESET}{' '*(20 - int(round(p.WATER/5)))}")

def printMap():
    printFoodAndStamina()
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
    printAt(map_width//2-len(p.NAME),2, f"Partie de {p.NAME}!")
    printAt(map_width//2//2, map_height+5,f'Y: {p.POS_Y} | X: {p.POS_X} | F: {round(p.FOOD)} | S: {round(p.STAMINA)} | W: {round(p.WATER)}\033[K')

def printAnimation(text):
    for letter in text:
        print(letter, end="", flush=True)
        if letter == ",":
            sleep(0.1)
        if letter == "." or letter =="!" or letter =="?":
            sleep(0.3)
        else:
            sleep(0.02)
