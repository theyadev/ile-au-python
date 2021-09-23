import numpy as np
import os
import msvcrt


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def getName():
    n = input(f"Quel est ton pseudonyme ?")
    try:
        n = int(n)
        print('Nom invalide.\n\n')
        return getName()
    except:
        return n

#nom = getName()


# input Taille de la carte
n, m = 30, 50
M = np.zeros((n, m))

# Cailloui
M[0:(n//15), :] = 1
M[0:int(2./3*n), 0:(m//25)] = 1
M[0:int(2./3*n), m-m//25:m] = 1

# O
M[int(2./3*n):, 0:(m//25)] = 2
M[int(2./3*n):, m-m//25:m] = 2
M[n-(n//15):n, :] = 2

# riviairt
pourcentage = 0.5
M[(n//15): int(1./3*n),      int(1./3*n):(int(1./3*n)+(m//25))] = 2
M[(int(1./3*n)-n//30): (int(1./3*n)+n//15-n//30),
  (int(1./3*n)+(n//15)-m//50): int(pourcentage*m)-m//50] = 2
M[(int(1./3*n)+n//15-n//15):, int(pourcentage*m)-m//25: int(pourcentage*m)] = 2


# test
M[25, 45] = 5

'''
0 = Terrain
1 = Caillasse
2 = L'eau
3 = Foret
4 = Sable
5 = Defi
'''
p = {
    "pos": {
        "x": m-m//25-1,
        "y": n-n//15-1
    }
}


def printMap():
    cls()
    for i in range(len(M)):
        l = ""
        for j in range(len(M[i])):
            if j == p["pos"]["x"] and i == p["pos"]["y"]:
                l += "😁"
            elif M[i][j] == 0:
                l += "  "
            elif M[i][j] == 1:
                l += "🔳"
            elif M[i][j] == 2:
                l += "🟦"
            elif M[i][j] == 3:
                l += "🟩"
            elif M[i][j] == 5:
                l += "❌"
        print(l)
    print('Haut: "z", Gauche: "q", Bas: "s", Droite:"d" | Inventaire: "e" | Quitter: "l"')


def collision(x, y):
    pos = M[p["pos"]["y"]+y, p["pos"]["x"]+x]
    if pos != 1 and pos != 2:
        return False
    else:
        return True


def move(x, y):
    if collision(x, y) == False:
        p["pos"]["x"] += x
        p["pos"]["y"] += y
        pos = M[p["pos"]["y"], p["pos"]["x"]]
        if (pos == 5):
            printMap()
            print('DEFI !!!!!!!!!!!')
        else:
            printMap()
    else:
        printMap()


def commande():
    command = bytes.decode(msvcrt.getch())
    if command == "l":
        print('Quitter')
        exit()
    elif command == "e":
        print("Inventaire")
        return commande()
    elif command == "q":
        move(-1, 0)
        return commande()
    elif command == "d":
        move(1, 0)
        return commande()
    elif command == "z":
        move(0, -1)
        return commande()
    elif command == "s":
        move(0, 1)
        return commande()
    else:
        return commande()


def init():
    printMap()
    commande()


init()
