import sys

sys.path.append('./Class/')
sys.path.append('./functions/')
sys.path.append('./minigames/')

from userInput import userInput
from settings import *
from prints import printMap, printAnimation

def main():
    clear()

    textContinue = '\nAppuyez sur entrée pour continuer...'
    texts = ["Ce matin, tu n'as pas été réveillé par les mouvements du navire (ton dernier souvenir est de t’être endormi sur la confortable couchette de ta cabine à bord de l’Argo), mais par le bruit des vagues, la chaleur du soleil et le champ des oiseaux...\n\n",
             "Il semble que tu ne sois plus sur le bateau.\n\n",
             "Tu es allongé sur une plage !\n\n",
             "Tu te redresses doucement, et, un peu aveuglé par le soleil, tu regardes autour de toi. D'un côté la mer… de l'autre un paysage sauvage, en partie steppe, en partie jungle. Assez loin, au-delà des arbres, tu penses apercevoir des montagnes.\n\n",
             ]
    #for text in texts:
    #    printAnimation(text)
    #input(textContinue)
    printMap()
    userInput()


if __name__ == '__main__':
    main()
