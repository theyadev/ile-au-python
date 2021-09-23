import settings
import sys

sys.path.append('./functions/')

from userInput import userInput
from map import printMap
from getName import getName
from clear import clear

settings.init()


def init():
    p = {
        "name": getName(),
        "pos": {
            "x": settings.m-settings.m//25-1,
            "y": settings.n-settings.n//15-1
        }
    }

    clear()
    print(f"Ce matin, tu n'as pas été réveillé par les mouvements du navire (ton dernier souvenir est de t’être endormi sur la confortable couchette de ta cabine à bord de l’Argo), mais par le bruit des vagues, la chaleur du soleil et le champ des oiseaux…\n\n")
    input('Appuyez sur entrée pour continuer...')
    clear()
    print("Il semble que tu ne sois plus sur le bateau.\n\n")
    input('Appuyez sur entrée pour continuer...')
    clear()
    print("Tu es allongé sur une plage !\n\n")
    input('Appuyez sur entrée pour continuer...')
    clear()
    print("Tu te redresses doucement, et, un peu aveuglé par le soleil, tu regardes autour de toi. D'un côté la mer… de l'autre un paysage sauvage, en partie steppe, en partie jungle. Assez loin, au-delà des arbres, tu penses apercevoir des montagnes.\n\n")
    input('Appuyez sur entrée pour continuer...')
    printMap(p)
    userInput(p)


if __name__ == '__main__':
    init()
