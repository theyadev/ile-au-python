import json
import os
from random import randint, seed


def checkChallengesCollision(challenges, x, y):
    returning_value = ""
    for c in challenges:
        if c["completed"] == True:
            continue
        if x == c["pos"]["x"] and y == c["pos"]["y"]:
            returning_value = c["name"]
    return returning_value


def initMap(p_seed=10):
    M = []
    seed(p_seed)
    with open('map.json') as mattrix:
        data = json.load(mattrix)
        M = []
        for index in range(len(data)):
            for i in data[index]:
                for l in i:
                    try:
                        if int(l) == 3:
                            random_nmber = randint(0, 5)
                            if random_nmber <= 4:
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


format_prefix = "\033["
position_suffix = "H"


def printAt(x, y, text, size):
    print(f"{format_prefix}{y};{x+size}{position_suffix}{text}")


def printMap():
    map_height = 30
    map_width = 50
    map_mattrix = initMap()
    challenges = initChallenges()
    # print((len(map_mattrix) + 5) * "\033[A" , end="")
    map_str = ""
    for y in range(len(map_mattrix)):
        row = ""
        for x in range(len(map_mattrix[y])):
            map_elem = map_mattrix[y][x]
            if x == 10 and y == 25:
                if map_elem == 2:
                    printAt(x+2,y+2,"a", 2)
                else:
                    printAt(x+2,y+2,"a", 2)
            elif checkChallengesCollision(challenges, x, y):
                # TODO: X Rouge
                printAt(x+2,y+2,"x", 2)
            elif map_elem == 0:
                printAt(x+2,y+2," ", 2)
            elif map_elem == 1:
                # TODO: BG Gris
                printAt(x+2,y+2, "o", 2)
            elif map_elem == 2:
                # TODO: BG Bleu
                printAt(x+2,y+2,"m", 2)
            elif map_elem == 3:
                # TODO: f Vert
                printAt(x+2,y+2,"f", 2)
            elif map_elem == 4:
                # TODO: petit char vert aussi
                printAt(x+2,y+2,"f", 2)
            elif map_elem == 5:
                # TODO: BG Jaune
                printAt(x+2,y+2,"s", 2)
        map_str += row + "\n"
    print(f"Partie de Theya !")
    # print(map_str)
    print('Haut: "z", Gauche: "q", Bas: "s", Droite:"d" | Inventaire: "e" | Quitter: "l"')


os.system('cls')
printMap()
