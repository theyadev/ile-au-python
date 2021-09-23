import msvcrt
import settings
from clear import cls
from map import printMap

settings.init()

def getName():
    n = input(f"Quel est ton pseudonyme ?")
    try:
        n = int(n)
        print('Nom invalide.\n\n')
        return getName()
    except:
        return n

#nom = getName()

p = {
    "pos": {
        "x": settings.m-settings.m//25-1,
        "y": settings.n-settings.n//15-1
    }
}


def collision(x, y):
    pos = settings.M[p["pos"]["y"]+y, p["pos"]["x"]+x]
    if pos != 1 and pos != 2:
        return False
    else:
        return True


def move(x, y):
    if collision(x, y) == False:
        p["pos"]["x"] += x
        p["pos"]["y"] += y
        pos = settings.M[p["pos"]["y"], p["pos"]["x"]]
        if (pos == 5):
            cls()
            print('DEFI !!!!!!!!!!!')
        else:
            printMap(p)


def commande():
    command = bytes.decode(msvcrt.getch())
    if command == "l":
        cls()
        print('Quitter')
        exit()
    elif command.lower() == "e":
        print("Inventaire")
        return commande()
    elif command.lower() == "q":
        move(-1, 0)
        return commande()
    elif command.lower() == "d":
        move(1, 0)
        return commande()
    elif command.lower() == "z":
        move(0, -1)
        return commande()
    elif command.lower() == "s":
        move(0, 1)
        return commande()
    else:
        return commande()


def init():
    printMap(p)
    commande()

if __name__ == '__main__':
    init()
