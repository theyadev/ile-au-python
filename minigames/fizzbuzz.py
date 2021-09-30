from random import randint,seed
from time import sleep


def startGame(player_name):
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

    def round(r):
        if len(players_list) == 1:
            return players_list[0][0]
        print(f"Début du round {r}")
        i = 0
        for n in range(1, 1000):   
                answer = str(n)
                sleep(0.3)
                if n % 3 == 0 and n % 5 == 0:
                    answer += "FizzBuzz"
                elif n % 3 == 0:
                    answer += "Fizz"
                elif n % 5 == 0:
                    answer += "Buzz"
                random_number = randint(0,100)

                if random_number <= players_list[i][1]:
                    print(f"{players_list[i][0]}: {answer}")
                else:
                    print(f"{players_list[i][0]} a perdu !!!!\n\n")
                    players_list.pop(i)
                    return round(r+1)
                if i == len(players_list) -1:
                    i -= i
                else:
                    i+= 1
                
        
    return round(1)
