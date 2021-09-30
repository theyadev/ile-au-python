import json
from random import randint, seed


def initMap():
    M = []
    seed(5)
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

# TODO: Si player.json vide ou inexistant, le creer
def initPlayer(reset=False):
    if reset == True:
        with open("player.json", "w") as p:
            default_player = {
                "name": None,
                "pos": {
                    "x": 38,
                    "y": 24
                }
            }
            json.dump(default_player, p, ensure_ascii=False, indent=4)
            return default_player
    else:
        with open("player.json") as p:
            data = json.load(p)
            return data
