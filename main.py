import sys

sys.path.append('./Class/')
sys.path.append('./functions/')
sys.path.append('./minigames/')

from userInput import userInput
from settings import *
from prints import printMap, printAnimation, printBoard

def main():
    clear()

    items_id_to_give = [6,7,8,9]
    if p.INVENTORY[items_id_to_give[0]-1].QUANTITY == 0:
        textContinue = '\nAppuyez sur entrée pour continuer...'
        texts = ["Ce matin, tu n'as pas été réveillé par les mouvements du navire (ton dernier souvenir est de t’être endormi sur la confortable couchette de ta cabine à bord de l’Argo), mais par le bruit des vagues, la chaleur du soleil et le champ des oiseaux...\n\n",
                "Il semble que tu ne sois plus sur le bateau.\n\n",
                "Tu es allongé sur une plage !\n\n",
                "Tu te redresses doucement, et, un peu aveuglé par le soleil, tu regardes autour de toi. D'un côté la mer... de l'autre un paysage sauvage, en partie steppe, en partie jungle. Assez loin, au-delà des arbres, tu penses apercevoir des montagnes.\n\n",
                "Tu fais un rapide bilan de ta situation : outre les vêtements que tu as sur toi, tu trouves un sac à dos avec :\n",
                "une bouteille vide en verre,\n",
                "et un petit couteau multifonctions de bonne facture\n\n",
                "Un peu plus loin, posée sur une pierre, se trouve une mallette contenant :\n",
                "ton ordinateur portable (oui, il y a du réseau sur cette île),\n",
                "et un système de recharge photovoltaïque\n\n",
                "Enfin, glissée à l'intérieur du couvercle de la mallette se trouve une carte grossière plastifiée\n\n",
                "Il est clair que tu n’es pas arrivé ici par hasard, ce n'est pas un naufrage, on t’a déposé sur cette plage. Mais entre le moment où tu t’es endormi et ton réveil il y a quelques minutes, c'est le trou noir...\n",]
        for text in texts:
            printAnimation(text)
        input(textContinue)

        for item_id in items_id_to_give:
            for item in p.INVENTORY:
                if item.ID == item_id:
                    item.QUANTITY += 1
    clear()
    printBoard()
    printMap()
    userInput()


if __name__ == '__main__':
    main()
