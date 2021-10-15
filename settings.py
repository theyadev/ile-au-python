import json
import os
from random import randint, seed
from Player import Player
from Item import Item
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def getChallengesPos(x,y):
    challenges = initChallenges()
    y_pos = [chall['pos']['y'] for chall in challenges]
    x_pos = [chall['pos']['x'] for chall in challenges]
    for i in range(len(y_pos)):
        if x == x_pos[i] and y == y_pos[i]:
            return True
    return False

def initMap(p_seed):
    M = []
    seed(p_seed)
    try:
        with open('./Data/map.json') as mattrix:
            data = json.load(mattrix)
            for y in range(len(data)):
                for x in range(len(data[y][0])):
                    try:
                        if int(data[y][0][x]) == 3:
                            random_nmber = randint(0, 10)
                            if random_nmber <= 8 or getChallengesPos(x,y) == True:
                                M[y].append(int(data[y][0][x]))
                            else:
                                M[y].append(4)
                        else:
                            M[y].append(int(data[y][0][x]))
                    except:
                        M.insert(y, [])
                        M[y].append(int(data[y][0][x]))
    except:
        return print('Il y a eu un probleme en chargeant la map ! ')
    return M

# TODO: Si challenges.json vide ou inexistant, le creer


def initChallenges(reset=False):
    try:
        if reset == True:
            with open("./Data/challenges.json", "r+", encoding="utf-8") as challenges:
                data = json.load(challenges)

                for index in range(len(data)):
                    data[index]["completed"] = False

                challenges.seek(0)
                json.dump(data, challenges, ensure_ascii=False, indent=4)
                challenges.truncate()
                return data
        else:
            with open("./Data/challenges.json", encoding="utf-8") as challenges:
                data = json.load(challenges)
                return data
    except:
        return print("Les challenges n'ont pas pus charger correctement.")
# TODO: Si player.json vide ou inexistant, le creer

def initItems():
    try:    
        with open('./Data/items.json', encoding="utf-8") as items_json:
            items_list = []
            items = json.load(items_json)
            for item in items:
                items_list.append(Item(item['NAME'], item['DESC'], item['WEIGHT'], 0, item['CHAR'], item['ID']))
            return items_list
    except:
        return print("Les items n'ont pas pus charger correctement.")

def initPlayer(reset=False):
    try: 
        if reset == True:
            with open("./Data/player.json", "w", encoding="utf-8") as p:
                items = initItems()
                default_player = Player(None, 38, 24, round(time.time() * 1000), inventory=items)
                json.dump(default_player.toJson(), p, ensure_ascii=False, indent=4)
                return default_player
        else:
            with open("./Data/player.json", encoding="utf-8") as p:
                data = json.load(p)
                return Player(data["NAME"], data['POS_X'], data["POS_Y"], data['SEED'], data['FOOD'], data['STAMINA'], data['WATER'], [Item(item['NAME'], item['DESC'], item['WEIGHT'], item['QUANTITY'], item['CHAR'], item['ID'])for item in data['INVENTORY']], data['MAP_MATTRIX'], data['RANDOM_ITEMS'])
    except:
        return print("Le joueur n'as pas pus charger correctement.")

def spawnItems():
    seed(p.SEED)
    items_list = initItems()
    random_ones = '01'
    random_items = []
    for i in range(len(items_list)):
        if str(i) in random_ones:
            random_nb = randint(5, 15)
            for j in range(random_nb):
                random_x = 5
                random_y = 0
                while str(p.MAP_MATTRIX[random_y][random_x]) in "1249":
                    random_x = randint(0, len(p.MAP_MATTRIX[0])-  1)
                    random_y = randint(0, len(p.MAP_MATTRIX) - 1)
                random_items.append((i, random_x, random_y))
    return random_items

def save():
    try:    
        with open('./Data/player.json', 'w', encoding="utf-8") as json_file:
            json.dump(p.toJson(), json_file, ensure_ascii=False, indent=4)
        return
    except:
        return print("La sauvegarde n'a pas pus s'effectuer.")


p = initPlayer()

clear()
os.system("mode con cols=100 lines=40")
if p.NAME == None:
    p.getName()
else:
    continue_game = input(f"Voulez vous reprendre avec le profil de {p.NAME} ? ").lower()

    if continue_game == "non" or continue_game == "n":
        start_new_game = input(f"Etes-vous sur de vouloir ecraser la sauvegarde de {p.NAME} ?! ").lower()
        if start_new_game == "o" or start_new_game == "oui":
            initChallenges(True)
            p = initPlayer(True)
            p.MAP_MATTRIX = initMap(p.SEED)
            p.RANDOM_ITEMS = spawnItems()
            p.getName()

if p.MAP_MATTRIX == None:
    p.MAP_MATTRIX = initMap(p.SEED)
if p.RANDOM_ITEMS == None:
    p.RANDOM_ITEMS = spawnItems()


"""

Every Variables

"""

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

collision_numbers = "124"
commands = {
    "z": "Haut",
    "q": "Gauche",
    "s": "Bas",
    "d": "Droite",
    "e": "Inventaire",
    "r": "Repos",
    "l": "Quitter"
}

commands_inventory = {
    "Flêche Haut": "Haut",
    "Flêche Bas": "Bas",
    "Entrée": "Utiliser",
    "t": "Jeter",
    "q": "Quitter"
}

map_height = len(p.MAP_MATTRIX)
map_width = len(p.MAP_MATTRIX[0])
map_margin = 4

board_width = map_width*2
board_height = map_height+map_margin+1

range_x = map_width + map_margin*2

range_x_2 = (((board_width-(map_width+map_margin*2)))//2)

info_height = 7
info_text = "Statistiques"

food_name = "Nourriture"
pos_food_y = 4

stamina_name = "Énergie"
pos_stamina_y = pos_food_y+1

water_name = "Soif"
pos_water_y = pos_stamina_y+1

inv_text = "Inventaire"
inv_height = board_height - info_height - len(commands) - 6

commands_text = "Commandes"

items_id_to_give = [6,7,8,9]

pointer = "\033[5m←\033[0m (Entrée)"

clear()
