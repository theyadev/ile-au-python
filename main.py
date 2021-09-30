from settings import *
import sys
import time

sys.path.append('./functions/')

from userInput import userInput
from map import printMap
from getName import getName
from clear import clear



def writeAnimation(t):
    for l in t:
        print(l, end="", flush=True)
        if l == ",":
            time.sleep(0.1)
        if l == "." or l =="!" or l =="?":
            time.sleep(0.3)
        else:
            time.sleep(0.02)


def startGame():
    p = initPlayer()
    reset = False
    if p["name"] == None:
        p["name"] = getName()
    else:  
        res = input(f"Voulez vous reprendre avec le profil de {p['name']} ? ")

        if res.lower() == "non" or res.lower() == "n":
                res2 = input(f"Etes-vous sur de vouloir ecraser la sauvegarde de {p['name']} ?! ")
                if res2.lower() == "o" or res2.lower() == "oui":
                    reset = True
                    initChallenges(reset)
                    p = initPlayer(reset)
                    p["name"] = getName()
    
    M = initMap(p["seed"])
        
    clear()

    textContinue = '\nAppuyez sur entrée pour continuer...'
    texts = ["Ce matin, tu n'as pas été réveillé par les mouvements du navire (ton dernier souvenir est de t’être endormi sur la confortable couchette de ta cabine à bord de l’Argo), mais par le bruit des vagues, la chaleur du soleil et le champ des oiseaux...\n\n",
             "Il semble que tu ne sois plus sur le bateau.\n\n",
             "Tu es allongé sur une plage !\n\n",
             "Tu te redresses doucement, et, un peu aveuglé par le soleil, tu regardes autour de toi. D'un côté la mer… de l'autre un paysage sauvage, en partie steppe, en partie jungle. Assez loin, au-delà des arbres, tu penses apercevoir des montagnes.\n\n",
             ]
    #for text in texts:
    #    writeAnimation(text)
    #input(textContinue)
    printMap({ "map": M}, p)
    userInput(p, { "map": M})


if __name__ == '__main__':
    startGame()
