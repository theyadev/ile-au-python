import json
from Colors import TextColors
from settings import p

def startChallenge(challenge):
    module = __import__(challenge["name"])
    player_name = p.NAME
    winner = module.startGame(player_name)
    
    if winner == player_name:
        print(f'{TextColors.GREEN}Bravo !!! Vous avez gagner !{TextColors.RESET}')

        with open('./Data/challenges.json','r+', encoding="utf-8") as json_file:
            data = json.load(json_file)
            for index, item in enumerate(data): 
                if item['name'] == challenge["name"]:
                    break
            else:
                index = -1

            data[index]["completed"] = True
            json_file.seek(0)
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            json_file.truncate()

        if challenge['reward']:
            p.INVENTORY[challenge['reward']-1].QUANTITY += 1

        input("\nAppuyez sur Entrée pour continuer... ")

        return
    else:
        if winner:
            print(f'Le gagnant est: {TextColors.GREEN}{winner}{TextColors.RESET} !')

        print(f'{TextColors.RED}Vous avez perdu !{TextColors.RESET} Voulez-vous rejouer ? (oui/non) ')

        res = input()

        if res.lower() == "oui" or res.lower() == "o":
            startChallenge(challenge)
        elif res.lower() == "non" or res.lower() == "n":
            print("Aurevoir ! C'était une belle partie !\n\n")
            return
        else:
            print("Tu n'as pas répondu oui ni non, je vais donc me désactiver ! Aurevoir !\n\n")
            return
