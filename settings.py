import json
import os
from random import randint, seed
from Player import Player
from Item import Item
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def initMap(p_seed):
    M = []
    seed(p_seed)
    with open('map.json') as mattrix:
        data = json.load(mattrix)
        M = []
        for index in range(len(data)):
            for y in data[index]:
                for l in y:
                    try:
                        if int(l) == 3:
                            random_nmber = randint(0, 10)
                            if random_nmber <= 8:
                                M[index].append(int(l))
                            else:
                                M[index].append(4)
                        else:
                            M[index].append(int(l))
                    except:
                        M.insert(index, [])
                        M[index].append(int(l))

    return M

# TODO: Si challenges.json vide ou inexistant, le creer


def initChallenges(reset=False):
    if reset == True:
        with open("challenges.json", "r+") as challenges:
            data = json.load(challenges)

            for index in range(len(data)):
                data[index]["completed"] = False

            challenges.seek(0)
            json.dump(data, challenges, ensure_ascii=False, indent=4)
            challenges.truncate()
            return data
    else:
        with open("challenges.json") as challenges:
            data = json.load(challenges)
            return data

# TODO: Si player.json vide ou inexistant, le creer

def initItems():
    with open('items.json', encoding="utf-8") as items_json:
        items_list = []
        items = json.load(items_json)
        for item in items:
            items_list.append(Item(item['NAME'], item['DESC'], item['WEIGHT'], 0))
        return items_list

def initPlayer(reset=False):
    if reset == True:
        with open("player.json", "w", encoding="utf-8") as p:
            items = initItems()
            default_player = Player(None, 38, 24, round(time.time() * 1000), inventory=items)
            json.dump(default_player.toJson(), p, ensure_ascii=False, indent=4)
            return default_player
    else:
        with open("player.json") as p:
            data = json.load(p)
            return Player(data["NAME"], data['POS_X'], data["POS_Y"], data['SEED'], data['FOOD'], data['STAMINA'], data['WATER'], [Item(item['NAME'], item['DESC'], item['WEIGHT'], item['QUANTITY'])for item in data['INVENTORY']])


def save():
    with open('./player.json', 'w') as json_file:
        json.dump(p.toJson(), json_file, ensure_ascii=False, indent=4)
    return

p = initPlayer()
map_mattrix = initMap(p.SEED)
collision_numbers = "124"

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
            p.getName()
clear()
