from clear import clear
from move import move
import msvcrt


def userInput(p):
    command = ""
    try:
        command = bytes.decode(msvcrt.getch()).lower()
    except:
        return userInput(p)

    if command == "l":
        clear()
        print('Quitter')
        exit()
    elif command == "e":
        clear()
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
