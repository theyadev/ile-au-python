from settings import *
from startChallenge import startChallenge
from prints import printMap, printFoodAndStamina, printBoard, printAt, printAll
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
        pointer = "\033[5m←\033[0m (Entrée)"
        pointer_pos = 1
        menu = [item for item in p.INVENTORY if item.QUANTITY > 0]

        inventory_x = map_width+map_margin*2+1

        def resetPointer(reset_all = False):
            for i in range(len(menu)):
                if reset_all == False and i == pointer_pos -1:
                    continue
                printAt(inventory_x + len(menu[i].NAME)+len(str(menu[i].QUANTITY))+2,info_height + 3 + i, " "*(len(pointer)+2))

        while True:
            if len(menu) == 0:
                break
            printAt(inventory_x +len(menu[pointer_pos-1].NAME)+len(str(menu[pointer_pos-1].QUANTITY))+4, info_height + 2 + pointer_pos, pointer)
            resetPointer()
            command = ord(msvcrt.getch())

            if command == 13:
                if str(pointer_pos-1) in "".join([str(i) for i in range(len(menu))]):
                    menu[pointer_pos-1].use(p)
                    pass
                resetPointer(True)
                break
            elif command == 72:
                if pointer_pos == 1:
                    continue
                else:
                    pointer_pos -= 1
            elif command == 80:
                if pointer_pos == len(menu):
                    continue
                else:
                    pointer_pos += 1
            elif command == 108:
                quit()

        printAll()
        return userInput()
    elif command == "q":
        movement = p.move(-1, 0, initChallenges())
        useMovement(movement)
    elif command == "d":
        movement = p.move(1, 0, initChallenges())
        useMovement(movement)
    elif command == "z":
        movement = p.move(0, -1, initChallenges())
        useMovement(movement)
    elif command == "s":
        movement = p.move(0, 1, initChallenges())
        useMovement(movement)
    else:
        return userInput()
