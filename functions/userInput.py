from settings import *
from startChallenge import startChallenge
from prints import printEndScreen, printMap, printFoodAndStamina, printBoard, printAt, printAll
import msvcrt
from time import sleep

def useMovement(movement):
    if type(movement) is bool:
        if p.FOOD <= 0 or p.WATER <=0:
            printEndScreen()
        else:
            printMap()
        return
    else:
        clear()
        startChallenge(movement)
        clear()
        printBoard()
        printMap()
        return

def restPlayer(p):
    while p.STAMINA < 100:
        if p.rest(1) == False: 
            break
        p.FACING = "idle"
        printFoodAndStamina()
        printMap()
        sleep(1)
    return

def inventoryInput():
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

        if command == 113:
            resetPointer(True)
            break
        elif command == 81:
            resetPointer(True)
            break
        elif command == 13:
            if str(pointer_pos-1) in "".join([str(i) for i in range(len(menu))]):
                item_id = menu[pointer_pos-1].ID
                remove_nb = 0
                if item_id == 2:
                    if p.FOOD + 10 <= 100:
                        p.FOOD += 10
                        remove_nb = 1
                elif item_id == 1:
                    if p.WATER+ 10 <= 100:
                        p.WATER +=10
                        remove_nb = 1

                menu[pointer_pos-1].remove(remove_nb)
                
            resetPointer(True)
            break
        elif command == 84 or command == 116:
            if str(pointer_pos-1) in "".join([str(i) for i in range(len(menu))]):
                item_id = menu[pointer_pos-1].ID
                p.RANDOM_ITEMS.append((item_id-1, p.POS_X, p.POS_Y))

                menu[pointer_pos-1].remove(1)
                
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
            break

def userInput():
    while True:
        command = ""
        try:
            command = bytes.decode(msvcrt.getch()).lower()
        except:
            continue

        if command == "l":
            clear()
            print('Sauvegarde en cours...')
            save()
            print("Quitter...")
            exit()
        elif command == 'r':         
            restPlayer(p)
            continue
        elif command == "e":
            
            inventoryInput()
            printAll()
            continue
        elif command == "q":
            movement = p.move(-1, 0, initChallenges())
            if movement == True:
                p.FACING = "left"
            useMovement(movement)
        elif command == "d":
            movement = p.move(1, 0, initChallenges())
            if movement == True:
                p.FACING = "right"
            useMovement(movement)
        elif command == "z":
            movement = p.move(0, -1, initChallenges())
            if movement == True:
                p.FACING = "up"
            useMovement(movement)
        elif command == "s":
            movement = p.move(0, 1, initChallenges())
            if movement == True:
                p.FACING = "down"
            useMovement(movement)
        else:
            continue
