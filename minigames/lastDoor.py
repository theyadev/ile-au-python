from settings import p
from prints import printWinningScreen, printAnimation

def startGame(player_name):
    textContinue = '\nAppuyez sur entrée pour continuer...'
    texts = ["Tout au nord de la zone, à côté d’une magnifique cascade descendant de la montagne, tu remarques une grotte. Intrigué, tu y pénètres mais l’intérieur est très sombre. \n\n",
             "Heureusement, une torche et un silex pour l’allumer se trouvent sur une pierre près de l’entrée.\n",
             "Tu allumes donc la torche et tu t’enfonces dans la grotte. Au bout de quelques minutes, tu trouves une grosse porte en bois qui bloque le passage. Au milieu de cette porte, trois grosses serrures qui semblent refléter les couleurs de 3 métaux précieux : bronze, argent et or\n\n",
 ]
    for text in texts:
       printAnimation(text)
    input(textContinue)

    required_items = [3,4,5]
    for item_id in required_items:
        for item in p.INVENTORY:
            if item.ID == item_id:
                if item.QUANTITY == 0:
                    return "lastDoor"
                else:
                    item.QUANTITY -= 1
    printWinningScreen()
