from settings import *
from collision import collision, checkChallengesCollision
from startChallenge import startChallenge
from prints import printMap
import msvcrt


def move(x, y):
    if collision(x, y) == False:
        p.POS_X += x
        p.POS_Y += y
        challenge = checkChallengesCollision(
            initChallenges(), p.POS_X, p.POS_Y)
        if challenge:
            clear()
            startChallenge(challenge)
            clear()
            printMap()
            userInput()
        else:
            printMap()
            userInput()
    else:
        userInput()


def userInput():
    command = ""
    try:
        command = bytes.decode(msvcrt.getch()).lower()
    except:
        return userInput()

    if command == "l":
        clear()
        print('Sauvegarde en cours...')
        save()
        print("Quitter...")
        exit()
    elif command == "e":
        clear()
        print("Inventaire")
        return userInput()
    elif command == "q":
        move(-1, 0)
    elif command == "d":
        move(1, 0)
    elif command == "z":
        move(0, -1)
    elif command == "s":
        move(0, 1)
    else:
        return userInput()
