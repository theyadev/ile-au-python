from random import randint,seed
from settings import clear
from prints import printAnimation
from Colors import TextColors
import time


def startGame(player_name):
    clear()
    textContinue = '\nAppuyez sur entrée pour continuer...'
    texts = ["En haut de la falaise, en bordure de forêt et pas très loin de la plage, tu découvres la statue d’un Sphinx avec une grosse clé en bronze posée sur les pattes.\n\n",
             "Lorsque tu t’en approches, les yeux de la statue s’illuminent et une voix se fait entendre :\n",
             f"\033[23mBonjour explorateur ! Pour ouvrir la porte de la montagne, atteindre le cœur de l’île et rejoindre tes compagnons, tu devras tout d’abord prouver ta valeur individuelle en gagnant les 3 clés que tu obtiendras en relevant les défis appropriés. Ceci est le premier d’entre eux\033[0m\n\n",
             "Il est bien entendu impossible de prendre la clé (qui semble collée aux pattes du Sphinx) tant que le défi n’est pasgagné.\n\n",
             "La voix poursuit :\n",
            f"\033[23m3 fois de suite, tu devras deviner le nombre que j’ai en tête, tu as 8 essais par nombre, es-tu prêt ?\033[0m\n\n"]
    for text in texts:
       printAnimation(text)
    input(textContinue)
    clear()
    seed(round(time.time() * 1000))
    numbers_to_find = [randint(1,100),randint(1,100),randint(1,100)]
    number = 0
    for index, number_to_find in enumerate(numbers_to_find):
        clear()
        number_of_try = 0
        max_number_of_try = 8
        if index == 0:
            print(f"Devinez le nombre {TextColors.CYAN}entre 1 et 100{TextColors.RESET}, vous avez {TextColors.RED}{max_number_of_try}{TextColors.RESET} essais:".center(100), end="\n\n")
        else:
            print(f"Bravo ! Devinez le {TextColors.CYAN}nombre suivant{TextColors.RESET}:".center(100), end="\n\n")
        while number != number_to_find:
            if number_of_try >= max_number_of_try:
                return False
            try:
                number= int(input())
                if number < number_to_find:
                    print(f"{TextColors.BLUE}Plus haut !\n{TextColors.RESET}")
                elif number > number_to_find:
                    print(f"{TextColors.YELLOW}Plus bas !\n{TextColors.RESET}")
                elif number_to_find != numbers_to_find[-1]:
                    print('\nBravo ! Nombre à deviner suivant.\n\n')
                number_of_try += 1
            except:
                print("Ce n'est pas un nombre !")
    return player_name
