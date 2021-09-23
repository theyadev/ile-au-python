from clear import cls
from move import move
import msvcrt

def userInput(p):
    command = bytes.decode(msvcrt.getch()).lower()

    if command == "l":
        cls()
        print('Quitter')
        exit()
    elif command == "e":
        cls()
        print("Inventaire")
        return userInput(p)
    elif command == "q":
        move(-1, 0, p)
        return userInput(p)
    elif command == "d":
        move(1, 0, p)
        return userInput(p)
    elif command == "z":
        move(0, -1, p)
        return userInput(p)
    elif command == "s":
        move(0, 1, p)
        return userInput(p)
    else:
        return userInput(p)