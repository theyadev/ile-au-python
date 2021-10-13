from random import randint,seed
from settings import clear
from Colors import TextColors
import time


def startGame(player_name):
    seed(round(time.time() * 1000))
    numbers_to_find = [randint(1,100),randint(1,100),randint(1,100)]
    number = 0
    for index, number_to_find in enumerate(numbers_to_find):
        clear()
        number_of_try = 0
        max_number_of_try = 6
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
