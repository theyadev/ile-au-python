from random import randint,seed
import time
def startGame(player_name):
    seed(round(time.time() * 1000))
    numbers_to_find = [randint(1,100),randint(1,100),randint(1,100)]
    number = 0
    for number_to_find in numbers_to_find:
        number_of_try = 0
        max_number_of_try = 10
        print(f"Devinez le nombre entre 1 et 100, vous avez {max_number_of_try} essais:")
        while number != number_to_find:
            if number_of_try >= max_number_of_try:
                return False
            try:
                number= int(input())
                if number < number_to_find:
                    print("Plus haut !")
                elif number > number_to_find:
                    print("Plus bas !")
                elif number_to_find != numbers_to_find[len(numbers_to_find)-1]:
                    print('\nBravo ! Nombre à deviner suivant.\n\n')
                number_of_try += 1
            except:
                print("Ce n'est pas un nombre !")
    return player_name
