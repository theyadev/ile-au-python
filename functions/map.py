from settings import initChallenges
from collision import checkChallengesCollision

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
    challenges = initChallenges()
    print((len(map_mattrix) + 5) * "\033[A" , end="")
    map_str = ""
    for i in range(len(map_mattrix)):
        row = ""
        for j in range(len(map_mattrix[i])): 
            map_elem = map_mattrix[i][j]
            if j == p["pos"]["x"] and i == p["pos"]["y"]:
                if map_elem == 2:
                    row += "🛳️"
                else:
                    row += "😁"
            elif checkChallengesCollision(challenges, j ,i):
                row += "❌"
            elif map_elem == 0:
                row += "  "
            elif map_elem == 1:
                row += "🔳"
            elif map_elem == 2:
                row += "🟦"
            elif map_elem == 3:
                row += "🌴"
            elif map_elem == 4:
                row += "🌳"
            elif map_elem == 5:
                row += "🟡"
        map_str += row + "\n"
    print(f"Partie de {p['name']} !")
    print(map_str)
    print('Haut: "z", Gauche: "q", Bas: "s", Droite:"d" | Inventaire: "e" | Quitter: "l"')
    print(f'Position Y: {p["pos"]["y"]} | Position X: {p["pos"]["x"]}')
