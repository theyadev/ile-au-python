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
cross = "╬"

commands = {
    "z": "Haut",
    "q": "Gauche",
    "s": "Bas",
    "d": "Droite",
    "e": "Inventaire",
    "r": "Repos",
    "l": "Quitter"
}

map_height = len(p.MAP_MATTRIX)
map_width = len(p.MAP_MATTRIX[0])
map_margin = 4

board_width = map_width*2
board_height = map_height+map_margin+1

range_x = map_width + map_margin*2

info_height = 7
info_text = "Statistiques"

food_name = "Nourriture"
pos_food_y = 4

stamina_name = "Énergie"
pos_stamina_y = pos_food_y+1

water_name = "Soif"
pos_water_y = pos_stamina_y+1

inv_text = "Inventaire"
inv_height = board_height - info_height - len(commands) - 4

commands_text = "Commandes"


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
                if y > 1:
                    printAt(x, y, vertical)
            if x == board_width-1:
                if 1 < y < info_height:
                    printAt(x, y, vertical)
                elif 1 < y < info_height + inv_height:
                    printAt(x, y, vertical)
                elif 1 < y < board_height:
                    printAt(x, y, vertical)
            if y == 0:
                if x == 0:
                    printAt(x, y, up_left)
                elif x == range_x-1:
                    printAt(x, y, horizontal_bot)
                elif x == board_width-1:
                    printAt(x, y, up_right)
                elif x > 1:
                    printAt(x, y, horizontal)
            elif y == 3:
                if x == 0:
                    printAt(x, y, vert_right)
                elif x == range_x-1:
                    printAt(x, y, cross)
                elif x > 1 and x < range_x:
                    printAt(x, y, horizontal)
                elif x > 1 and x < board_width - 1:
                    printAt(x, y, horizontal)
                elif x == board_width - 1:
                    printAt(x,y, vert_left)
            elif y == info_height:
                if x == range_x-1:
                    printAt(x, y, vert_right)
                elif x == board_width-1:
                    printAt(x, y, vert_left)
                elif x >= range_x:
                    printAt(x, y, horizontal)
                elif x == 0:
                    printAt(x, y, vertical)
            elif y == info_height + 2:
                if x == range_x-1:
                    printAt(x, y, vert_right)
                elif x == board_width-1:
                    printAt(x, y, vert_left)
                elif x >= range_x:
                    printAt(x, y, horizontal)
                elif x == 0:
                    printAt(x, y, vertical)
            elif y == info_height + inv_height:
                if x == range_x-1:
                    printAt(x, y, vert_right)
                elif x == board_width-1:
                    printAt(x, y, vert_left)
                elif x >= range_x:
                    printAt(x, y, horizontal)
                elif x == 0:
                    printAt(x, y, vertical)
            elif y == info_height + inv_height + 2:
                if x == range_x-1:
                    printAt(x, y, vert_right)
                elif x == board_width-1:
                    printAt(x, y, vert_left)
                elif x >= range_x:
                    printAt(x, y, horizontal)
                elif x == 0:
                    printAt(x, y, vertical)
            elif y == board_height-1:
                if x == 1:
                    printAt(x, y, bot_left)
                elif x > 1 and x < range_x-1:
                    printAt(x, y, horizontal)
                elif x == range_x-1:
                    printAt(x, y, horizontal_up)
                elif x >= range_x and x < board_width-1:
                    printAt(x, y, horizontal)
                elif x == board_width-1:
                    printAt(x, y, bot_right)
    # Partie de
    printAt(map_width//2-len(p.NAME), 2, f"Partie de {p.NAME}!")

    # Statistiques
    printAt((map_width+(map_margin*2))+(((board_width-(map_width+map_margin*2)))//2)-(len(info_text)//2), 2, f"{info_text}")
    
    # Inventaire
    printAt((map_width+(map_margin*2))+(((board_width-(map_width+map_margin*2)))//2)-(len(inv_text)//2), info_height+1, f"{inv_text}")
    
    # Commandes
    printAt((map_width+(map_margin*2))+(((board_width-(map_width+map_margin*2)))//2)-(len(commands_text)//2), info_height+inv_height+ 1, f"{commands_text}")


def printFoodAndStamina():
    longest_stat = getLongestStat()
    printAt(range_x+1, pos_food_y, f"{food_name}{'.' * (len(longest_stat)+ 1-len(food_name))}│{TextColors.BLACK}{BackgroundColors.RED}{'∙'*(int(round(p.FOOD/5)))}{BackgroundColors.RESET_ALL}{f'{BackgroundColors.WHITE + TextColors.BLACK}∙{BackgroundColors.RESET_ALL}'*(20-int(round(p.FOOD/5)))}│ ({round(p.FOOD)}) ")
    printAt(range_x+1, pos_stamina_y, f"{stamina_name}{'.' * (len(longest_stat)+ 1-len(stamina_name))}│{TextColors.BLACK}{BackgroundColors.YELLOW}{'∙'*(int(round(p.STAMINA/5)))}{BackgroundColors.RESET_ALL}{f'{BackgroundColors.WHITE + TextColors.BLACK}∙{BackgroundColors.RESET_ALL}'*(20 - int(round(p.STAMINA/5)))}│ ({round(p.STAMINA)}) ")
    printAt(range_x+1, pos_water_y, f"{water_name}{'.' * (len(longest_stat)+ 1-len(water_name))}│{TextColors.BLACK}{BackgroundColors.CYAN}{'∙'*(int(round(p.WATER/5)))}{BackgroundColors.RESET_ALL}{f'{BackgroundColors.WHITE + TextColors.BLACK}∙{BackgroundColors.RESET_ALL}'*(20 - int(round(p.WATER/5)))}│ ({round(p.WATER)}) ")

def getIndexItem(x,y):
    for index,item in enumerate(p.RANDOM_ITEMS):
        if item[1] == x and item[2] == y:
            return index 
    return False

def printCommands():
    for index, (key, action) in enumerate(commands.items()):
        printAt(range_x+1, inv_height + info_height + index + 3, f"{key}: {action}")

def printInventory():
    col = 2
    curr_col = 0
    curr_row = 0
    weight = p.getWeight()
    for item in p.INVENTORY:
        if item.QUANTITY == 0:
            continue
        printAt(map_width+map_margin*2+1, info_height + 3 + curr_row, f"{item.NAME} x{item.QUANTITY}")
        curr_row += 1
    printAt(board_width-2-len(str(round(weight, 2)) + p.METRIC), info_height + inv_height-1, f"{round(weight, 2)}{p.METRIC}")

def printMap():
    printCommands()
    printFoodAndStamina()
    printInventory()
    challenges = initChallenges()
    for y in range(len(p.MAP_MATTRIX)):
        for x in range(len(p.MAP_MATTRIX[y])):
            map_elem = p.MAP_MATTRIX[y][x]
            style = ""
            txt = " "
            # Challenges
            if checkChallengesCollision(challenges, x, y):
                style = TextColors.RED
                txt = "X"
            elif getIndexItem(x,y):
                index = getIndexItem(x,y)
                index_item = p.RANDOM_ITEMS[index][0]
                items = initItems()
                txt = items[index_item].CHAR
            # Pierre
            elif map_elem == 1:
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
            printAt(x+map_margin, y+map_margin,
                    f'{style}{txt}{TextColors.RESET_ALL}')
    printAt(map_width//2//2, map_height+5,
            f'Y: {p.POS_Y} | X: {p.POS_X} | F: {round(p.FOOD)} | S: {round(p.STAMINA)} | W: {round(p.WATER)}\033[K')

def printAnimation(text):
    for letter in text:
        print(letter, end="", flush=True)
        if letter == ",":
            sleep(0.1)
        if letter == "." or letter == "!" or letter == "?":
            sleep(0.3)
        else:
            sleep(0.02)
