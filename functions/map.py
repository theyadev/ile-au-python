from clear import clear
import settings
# input Taille de la carte

'''
0 = Terrain
1 = Caillasse
2 = L'eau
3 = Foret
4 = Sable
5 = Defi
'''


def printMap(p):
    clear()
    for i in range(len(settings.M)):
        l = ""
        for j in range(len(settings.M[i])):
            if j == p["pos"]["x"] and i == p["pos"]["y"]:
                l += "😁"
            elif settings.M[i][j] == 0:
                l += "  "
            elif settings.M[i][j] == 1:
                l += "🔳"
            elif settings.M[i][j] == 2:
                l += "🟦"
            elif settings.M[i][j] == 4:
                l += "🟡"
            elif settings.M[i][j] == 3:
                l += "\033[92mf \033[0m"
            elif settings.M[i][j] == 5:
                l += "❌"
        print(l)
    print('Haut: "z", Gauche: "q", Bas: "s", Droite:"d" | Inventaire: "e" | Quitter: "l"')
