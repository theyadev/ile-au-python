import settings
import sys
import time

sys.path.append('./functions/')

from userInput import userInput
from map import printMap
from getName import getName
from clear import clear

settings.init()


def writeAnimation(t):
    for l in t:
        print(l, end="", flush=True)
        if l == ",":
            time.sleep(0.1)
        if l == ".":
            time.sleep(0.4)
        else:
            time.sleep(0.02)


def init():
    p = {
        "name": getName(),
        "pos": {
            "x": settings.m-settings.m//25-1,
            "y": settings.n-settings.n//15-1
        }
    }

    clear()

    textContinue = 'Appuyez sur entrée pour continuer...'
    texts = ["Ce matin, tu n'as pas été réveillé par les mouvements du navire (ton dernier souvenir est de t’être endormi sur la confortable couchette de ta cabine à bord de l’Argo), mais par le bruit des vagues, la chaleur du soleil et le champ des oiseaux…\n\n",
             "Il semble que tu ne sois plus sur le bateau.\n\n",
             "Tu es allongé sur une plage !\n\n",
             "Tu te redresses doucement, et, un peu aveuglé par le soleil, tu regardes autour de toi. D'un côté la mer… de l'autre un paysage sauvage, en partie steppe, en partie jungle. Assez loin, au-delà des arbres, tu penses apercevoir des montagnes.\n\n",
             ]
    for text in texts:
        writeAnimation(text)
        writeAnimation(textContinue)
        input()
        clear()
    printMap(p)
    userInput(p)


if __name__ == '__main__':
    init()
