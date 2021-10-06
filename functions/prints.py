from time import sleep
from settings import initChallenges
from challengesCollision import checkChallengesCollision
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
horizontal_up = "╩"
cross ="╬"

map_height = len(map_mattrix)
map_width = len(map_mattrix[0])
map_margin = 4

board_width = map_width*2
board_height = map_height+map_margin+1

range_x = map_width+ map_margin*2

info_height = 8

food_name = "Nourriture"
pos_food_y = 4

stamina_name = "Énergie"
pos_stamina_y = pos_food_y+1

water_name = "Soif"
pos_water_y = pos_stamina_y+1



inv_size =  15

def getLongestStat():
    if len(water_name) > len(stamina_name) and len(water_name) > len(food_name):
        return water_name
    elif len(stamina_name) > len(water_name) and len(stamina_name) > len(food_name):
        return stamina_name
    elif len(food_name) > len(water_name) and len(food_name) > len(stamina_name):
        return food_name

def printAt(x, y, text):
    print(f"{format_prefix}{y};{x}{position_suffix}{text}")

def printBoard():
    for y in range(board_height):
        for x in range(board_width):
            if x == 0 or x == range_x-1:
                if y >1:
                    printAt(x,y,vertical)
            if x == board_width-1:
                if 1<y<info_height:
                    printAt(x,y,vertical)
                elif 1<y<info_height + inv_size:
                    printAt(x,y,vertical)
                elif 1<y<board_height:
                    printAt(x,y,vertical)
            if y == 0:
                if x == 0:
                    printAt(x,y,up_left)
                elif x == range_x-1:
                    printAt(x,y,horizontal_bot)
                elif x == board_width-1:
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
            elif y == info_height:
                if x == range_x-1:
                    printAt(x,y, vert_right)
                elif x == board_width-1:
                    printAt(x,y,vert_left)
                elif x >= range_x:
                    printAt(x,y,horizontal)
                elif x == 0: printAt(x,y,vertical)
            elif y == info_height + inv_size:
                if x == range_x-1:
                    printAt(x,y, vert_right)
                elif x == board_width-1:
                    printAt(x,y,vert_left)
                elif x >= range_x:
                    printAt(x,y,horizontal)
                elif x == 0: printAt(x,y,vertical)
            elif y == board_height-1:
                if x == 1:
                    printAt(x,y,bot_left)
                elif x>1 and x < range_x-1:
                    printAt(x,y,horizontal)
                elif x == range_x-1:
                    printAt(x,y,horizontal_up)
                elif x >= range_x and x < board_width-1:
                    printAt(x,y,horizontal)
                elif x == board_width-1:
                    printAt(x,y,bot_right)


def printFoodAndStamina():
    longest_stat = getLongestStat() 
    printAt(range_x+1, pos_food_y, f"{food_name}{'.' * (len(longest_stat)+ 1-len(food_name))} {TextColors.BLACK}{BackgroundColors.RED}{'●'*(int(round(p.FOOD/5)))}{BackgroundColors.RESET_ALL}{' '*(20-int(round(p.FOOD/5)))} | {round(p.FOOD)}  ")
    printAt(range_x+1, pos_stamina_y, f"{stamina_name}{'.' * (len(longest_stat)+ 1-len(stamina_name))} {TextColors.BLACK}{BackgroundColors.YELLOW}{'●'*(int(round(p.STAMINA/5)))}{BackgroundColors.RESET_ALL}{' '*(20 - int(round(p.STAMINA/5)))} | {round(p.STAMINA)}  ")
    printAt(range_x+1, pos_water_y, f"{water_name}{'.' * (len(longest_stat)+ 1-len(water_name))} {TextColors.BLACK}{BackgroundColors.CYAN}{'●'*(int(round(p.WATER/5)))}{BackgroundColors.RESET_ALL}{' '*(20 - int(round(p.WATER/5)))} | {round(p.WATER)}  ")

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
