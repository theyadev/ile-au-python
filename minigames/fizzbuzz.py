from random import randint,seed
from prints import printAt, printAnimation
from time import sleep
from Colors import TextColors
from settings import *

game_board_height = 4
game_board_width = 100

center_size = [40,60]
def printGameBoard():
    for y in range(game_board_height):
        for x in range(game_board_width):
            if y == 1:
                if x == center_size[0]:
                    printAt(x, y, up_left)
                elif x == center_size[1]:
                    printAt(x, y, up_right)
                elif  center_size[0] < x < center_size[1]:
                    printAt(x, y, horizontal)
            elif y == game_board_height-1:
                if x == center_size[0]:
                    printAt(x, y, bot_left)
                elif x == center_size[1]:
                    printAt(x, y, bot_right)
                elif center_size[0] < x < center_size[1]:
                    printAt(x, y, horizontal)
            else:
                if x == center_size[0] or x == center_size[1]:
                    printAt(x, y, vertical)

def startGame(player_name):
    clear()
    textContinue = '\nAppuyez sur entrée pour continuer...'
    texts = ["En explorant la jungle, tu remarques une bande de singes braillards évoluant dans les arbres. En écoutant avec un peu plus d’attention, tu te rends comptes que les singes semblent articuler des nombres et que deux sons reviennent régulièrement : Fizz et Buzz...\n\n",
             "À un moment, les cris s’arrêtent et tu te retrouves subitement entouré par les singes.\n\n",
             "L’un d’eux, probablement le chef vu sa démarche assurée, descend de l’arbre et s’approche de toi. Il te toise un instant puis, du doigt, te désigne un endroit en hauteur. En levant la tête, tu aperçois une grosse clé en or, pendue à une solide liane, tu commences à chercher un moyen de grimper dans les arbres, mais cela déclenche une vive réaction de la part des singes. Il semble qu’ils ne soient pas disposés à te donner la clé comme ça !\n\n",
             "Il est bien entendu impossible de prendre la clé (qui semble collée aux pattes du Sphinx) tant que le défi n’est pasgagné.\n\n",
             "Tu te ravises alors, et le chef se rapproche de toi et commence à te parler...\n« Toi jouer ! Si gagner alors clé à toi ! »\nJouer ? Mais à quoi ?\nSemblant lire dans tes pensées, le chef dit alors « Nous montrer. » Puis il dit « 1 ». Un autre singe dans les arbres dit alors « 2 », puis un troisième « Fizz » et ainsi de suite : « 4 », « Buzz », « Fizz », « 7 », « 8 », « Fizz », « Buzz », « 11 », « 12 »... À ce moment, tous les autres singes se mettent à rire et celui qui vient d’annoncer 12 pousse un cri de déception et se retourne sur sa branche en boudant, puis le jeu recommence avec les singes restants : « 1 », « 2 », « Fizz »...\n\n",
         ]
    for text in texts:
       printAnimation(text)
    input(textContinue)
    clear()
    seed(randint(0, 100000))
    chief_monkeys = 1
    default_monkeys = 9

    players_list = []

    prob_chief_min = 70
    prob_chief_max = 90

    prob_default_min = 50
    prob_default_max = 60


    prob_player_min = 80
    prob_player_max = 95

    for i in range(default_monkeys):
        players_list.insert(randint(0, len(players_list)), [f"Singe N°{i+1}", randint(prob_default_min, prob_default_max)])
    for i in range(chief_monkeys):
        players_list.insert(randint(0, len(players_list)), [f"Chef Singe N°{i+1}", randint(prob_chief_min, prob_chief_max)])

    players_list.insert(randint(0, len(players_list)), [player_name, randint( prob_player_min, prob_player_max)])

    old_players_list = list(players_list)
    def round(r = 0, end=False):
        if end == True:
            return
        if len(players_list) == 1:
            return players_list[0][0]
        
        printAt(0, 2,f"Round {r}/{len(old_players_list)-1}".center(100))
        printGameBoard()

        i = 0
        for n in range(1, 1000):   
                sleep(0.3)
                random_number = randint(0,100)

                if random_number <= players_list[i][1] or n == 1:
                    answer = str(n)

                    if n % 3 == 0 and n % 5 == 0:
                        answer = "FizzBuzz"
                    elif n % 3 == 0:
                        answer = "Fizz"
                    elif n % 5 == 0:
                        answer = "Buzz"

                    printAt(0,n+3+(2*n-1),f"{TextColors.YELLOW}{players_list[i][0].center(100)}{TextColors.RESET}:")
                    printAt(0,n+4+(2*n-1), f"{TextColors.GREEN}{answer.center(100)}{TextColors.RESET}\n")
                else:
                    if players_list[i][0] == player_name:
                        printAt(0,n+3+(2*n-1),f"{TextColors.RED}{'Vous avez donné la mauvaise réponse !!!!'.center(100)}{TextColors.RESET}\n\n")
                        players_list.pop(i)
                        return round(end=True)
                    else:
                        printAt(0,n+3+(2*n-1),f"{TextColors.RED}{f'{players_list[i][0]} a donné la mauvaise réponse !!!!'.center(100)}{TextColors.RESET}\n\n")
                        
                        players_list.pop(i)
                        if len(players_list) > 1:
                            input('Round suivant... (Entrée)'.center(100))
                            clear()
                        
                        return round(r+1)
                if i == len(players_list) -1:
                    i -= i
                else:
                    i+= 1
                
        
    return round(1)
