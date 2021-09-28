import json

def init():
    global M

    with open('map.json') as mattrix:
        data = json.load(mattrix)
        M = []
        for index in range(len(data)):
            for i in data[index]:
                for l in i:
                    try:
                        M[index].append(int(l))
                    except:
                        M.insert(index, [])
                        M[index].append(int(l))