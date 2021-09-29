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
                            random_nmber = randint(0,5)
                            print(random_nmber)
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

def initChallenges():
    with open("challenges.json") as challenges:
        data = json.load(challenges)
        return data