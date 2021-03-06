from time import sleep
from settings import initChallenges
from challengesCollision import checkChallengesCollision
from Colors import *
from settings import *
import settings as Var

'''
0 = Terrain
1 = Caillasse
2 = L'eau
3 = Foret
4 = Sable
5 = Defi
'''

def getLongestStat():
    if len(water_name) > len(stamina_name) and len(water_name) > len(food_name):
        return water_name
    elif len(stamina_name) > len(water_name) and len(stamina_name) > len(food_name):
        return stamina_name
    elif len(food_name) > len(water_name) and len(food_name) > len(stamina_name):
        return food_name

def getIndexItem(x,y):
    for index,item in enumerate(p.RANDOM_ITEMS):
        if item[1] == x and item[2] == y:
            return index 
    return False

def printEndScreen():
    clear()
    print(f"{TextColors.RED}Vous avez perdu !{TextColors.RESET}")
    input("Appuyez sur entrée pour quitter...")
    Var.p = initPlayer(True)
    initChallenges(True)
    save()
    quit()

def printWinningScreen():
    clear()
    print(f"{TextColors.GREEN}Vous avez gagner !{TextColors.RESET}")
    input("Appuyez sur entrée pour quitter...")
    Var.p = initPlayer(True)
    initChallenges(True)
    save()
    quit()

def printAt(x, y, text):
    print(f"{format_prefix}{y};{x}{position_suffix}{text}")

def printBoard():
    for y in range(board_height):
        for x in range(board_width):
            if x == range_x+range_x_2:
                if y > info_height + inv_height:
                    printAt(x,y, vertical)
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
                if x == range_x+range_x_2:
                    printAt(x,y, horizontal_bot)
                elif x == range_x-1:
                    printAt(x, y, vert_right)
                elif x == board_width-1:
                    printAt(x, y, vert_left)
                elif x >= range_x:
                    printAt(x, y, horizontal)
                elif x == 0:
                    printAt(x, y, vertical)
            elif y == info_height + inv_height + 2+2:
                if x == range_x+range_x_2:
                    printAt(x,y, cross)
                elif x == range_x-1:
                    printAt(x, y, vert_right)
                elif x == board_width-1:
                    printAt(x, y, vert_left)
                elif x >= range_x:
                    printAt(x, y, horizontal)
                elif x == 0:
                    printAt(x, y, vertical)
            elif y == board_height-1:
                if x == range_x+range_x_2:
                    printAt(x,y, horizontal_up)
                elif x == 1:
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
    printAt(range_x+range_x_2-(len(info_text)//2), 2, f"{info_text}")
    
    # Inventaire
    printAt(range_x+range_x_2-(len(inv_text)//2), info_height+1, f"{inv_text}")
    
    # Commandes
    printAt(range_x+range_x_2-(len(commands_text)//2), info_height+inv_height+ 1, f"{commands_text}")

    # Carte
    printAt(range_x+range_x_2-(len(commands_text)//2+9), info_height+inv_height+ 1+2, f"Carte")

    # Inventaire
    printAt(range_x+range_x_2+(len(commands_text)//2+1), info_height+inv_height+ 1+2, f"Inventaire")

def printFoodAndStamina():
    longest_stat = getLongestStat()
    printAt(range_x+1, pos_food_y, f"{food_name}{'.' * (len(longest_stat)+ 1-len(food_name))}│{TextColors.BLACK}{BackgroundColors.RED}{'∙'*(int(round(p.FOOD/5)))}{BackgroundColors.RESET_ALL}{f'{BackgroundColors.WHITE + TextColors.BLACK}∙{BackgroundColors.RESET_ALL}'*(20-int(round(p.FOOD/5)))}│ ({round(p.FOOD)}) ")
    printAt(range_x+1, pos_stamina_y, f"{stamina_name}{'.' * (len(longest_stat)+ 1-len(stamina_name))}│{TextColors.BLACK}{BackgroundColors.YELLOW}{'∙'*(int(round(p.STAMINA/5)))}{BackgroundColors.RESET_ALL}{f'{BackgroundColors.WHITE + TextColors.BLACK}∙{BackgroundColors.RESET_ALL}'*(20 - int(round(p.STAMINA/5)))}│ ({round(p.STAMINA)}) ")
    printAt(range_x+1, pos_water_y, f"{water_name}{'.' * (len(longest_stat)+ 1-len(water_name))}│{TextColors.BLACK}{BackgroundColors.CYAN}{'∙'*(int(round(p.WATER/5)))}{BackgroundColors.RESET_ALL}{f'{BackgroundColors.WHITE + TextColors.BLACK}∙{BackgroundColors.RESET_ALL}'*(20 - int(round(p.WATER/5)))}│ ({round(p.WATER)}) ")

def printCommands():
    for index, (key, action) in enumerate(commands.items()):
        printAt(range_x+1, inv_height + info_height + index + 5, f"{key}: {action}")
    for index, (key, action) in enumerate(commands_inventory.items()):
        printAt(range_x+range_x_2+2, inv_height + info_height + index + 5, f"{key}: {action}")
        
def printInventory():
    curr_row = 0
    weight = p.getWeight()
    for item in p.INVENTORY:
        if item.QUANTITY == 0:
            continue
        printAt(map_width+map_margin*2+1, info_height + 3 + curr_row, f"{item.NAME} x{item.QUANTITY}     ")
        curr_row += 1
    max_row = inv_height - 2 - curr_row - 2
    if curr_row == 0:
        printAt(map_width+map_margin*2+1, info_height + 3 + curr_row, f"Vide...                ")
        curr_row += 1
    for i in range(max_row):
        printAt(map_width+map_margin*2+1, info_height + 3 + curr_row, f"{' '*(board_width-(map_width+map_margin*2)-5)}")
        curr_row += 1
    heavy_text = " Vous etes trop lourd ! "
    too_heavy = heavy_text if weight > p.MAX_WEIGHT else ' '*len(heavy_text)
    printAt(board_width-2-len(str(round(weight, 2)) + p.METRIC + too_heavy), info_height + inv_height-1, f"{TextColors.RED if too_heavy == heavy_text else ''}{BackgroundColors.WHITE if too_heavy == heavy_text else ''}{too_heavy}{TextColors.RESET_ALL}{round(weight, 2)}{p.METRIC}")

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
                txt = "∆"
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
            # Pont
            elif map_elem == 6:
                style = TextColors.WHITE
                txt = "░"

            # Joueur
            if x == p.POS_X and y == p.POS_Y:
                style += TextColors.RED
                if p.FACING == "up":
                    txt = "▲"
                elif p.FACING == "down":
                    txt = "▼"
                elif p.FACING == "left":
                    txt = "◄"
                elif p.FACING == "right":
                    txt = "►"
                else:
                    txt ="●"

            printAt(x+map_margin, y+map_margin, f'{style}{txt}{TextColors.RESET_ALL}')

    printAt(map_width//2//2, map_height+5, f'Y: {p.POS_Y} | X: {p.POS_X} | F: {round(p.FOOD)} | S: {round(p.STAMINA)} | W: {round(p.WATER)}\033[K')

def printAll():
    printBoard()
    printMap()
    printFoodAndStamina()
    printInventory()
    printCommands()

def printAnimation(text, speed = (0.05,0.2,0.01)):
    comma, dots, letters = speed
    for letter in text:
        print(letter, end="", flush=True)
        if letter == ",":
            sleep(comma)
        if letter == "." or letter == "!" or letter == "?":
            sleep(dots)
        else:
            sleep(letters)
