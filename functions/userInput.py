from settings import *
from collision import collision, checkChallengesCollision
from startChallenge import startChallenge
from prints import printMap, printFoodAndStamina
import msvcrt
from time import sleep


def move(x, y):
    if p.STAMINA <= 0: userInput()
    if collision(x, y) == False:
        p.POS_X += x
        p.POS_Y += y
        p.STAMINA -= 2 if p.STAMINA > 0 else 0
        p.FOOD -= 0.25 if p.FOOD > 0 else 0
        p.WATER -= 0.25 if p.WATER > 0 else 0
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
    elif command == 'r':         
        while p.STAMINA < 100:
            if p.rest(1) == False: 
                return userInput()
            
            printFoodAndStamina()
            printMap()
            time.sleep(1)
        return userInput()
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
