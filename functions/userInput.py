from clear import clear
from save import save
from settings import initChallenges
from collision import collision, checkChallengesCollision
from startChallenge import startChallenge
from map import printMap
import msvcrt

def move(x, y, p, settings):
    map_mattrix = settings['map']
    if collision(x, y, p, map_mattrix) == False:
        p.posX += x
        p.posY += y
        challenge = checkChallengesCollision(
            initChallenges(), p.posX, p.posY)
        if challenge:
            clear()
            startChallenge(challenge)
            clear()
            printMap(settings, p)
            userInput(p, settings)
        else:
            printMap(settings, p)
            userInput(p, settings)
    else:
        userInput(p, settings)


def userInput(p, settings):
    command = ""
    try:
        command = bytes.decode(msvcrt.getch()).lower()
    except:
        return userInput(p, settings)

    if command == "l":
        clear()
        print('Sauvegarde en cours...')
        save(p)
        print("Quitter...")
        exit()
    elif command == "e":
        clear()
        print("Inventaire")
        return userInput(p, settings)
    elif command == "q":
        move(-1, 0, p, settings)
    elif command == "d":
        move(1, 0, p, settings)    
    elif command == "z":
        move(0, -1, p, settings)
    elif command == "s":
        move(0, 1, p, settings)
    else:
        return userInput(p, settings)
