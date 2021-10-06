from settings import *
from startChallenge import startChallenge
from prints import printMap, printFoodAndStamina, printBoard
import msvcrt
from time import sleep

def useMovement(movement):
    if movement == False:
        printMap()
        return userInput()
    else:
        clear()
        startChallenge(movement)
        clear()
        printBoard()
        printMap()
        return userInput()

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
        movement = p.move(-1, 0, initChallenges(), map_mattrix, random_items, initItems())
        useMovement(movement)
    elif command == "d":
        movement = p.move(1, 0, initChallenges(), map_mattrix, random_items, initItems())
        useMovement(movement)
    elif command == "z":
        movement = p.move(0, -1, initChallenges(), map_mattrix, random_items, initItems())
        useMovement(movement)
    elif command == "s":
        movement = p.move(0, 1, initChallenges(), map_mattrix, random_items, initItems())
        useMovement(movement)
    else:
        return userInput()
