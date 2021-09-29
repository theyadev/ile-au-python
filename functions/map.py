from clear import clear
from collision import checkChallengesCollision
# input Taille de la carte

'''
0 = Terrain
1 = Caillasse
2 = L'eau
3 = Foret
4 = Sable
5 = Defi
'''

def printMap(settings, p):
    map_mattrix = settings['map']
    challenges = settings["challenges"]
    clear()
    map_str = ""
    for i in range(len(map_mattrix)):
        l = ""
        for j in range(len(map_mattrix[i])): 
            map_elem = map_mattrix[i][j]
            if j == p["pos"]["x"] and i == p["pos"]["y"]:
                if map_elem == 2:
                    l += "🛳️"
                else:
                    l += "😁"
            elif checkChallengesCollision(challenges, j ,i):
                l += "❌"
            elif map_elem == 0:
                l += "  "
            elif map_elem == 1:
                l += "🔳"
            elif map_elem == 2:
                l += "🟦"
            elif map_elem == 3:
                l += "🌴"
            elif map_elem == 4:
                l += "🌳"
            elif map_elem == 5:
                l += "🟡"
        map_str += l + "\n"
    print(map_str)
    print('Haut: "z", Gauche: "q", Bas: "s", Droite:"d" | Inventaire: "e" | Quitter: "l"')
    print(f'Position Y: {p["pos"]["y"]} | Position X: {p["pos"]["x"]}')
