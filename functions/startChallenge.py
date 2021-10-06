import json
from settings import p
def startChallenge(challenge_name):
    module = __import__(challenge_name)
    player_name = p.NAME
    winner = module.startGame(player_name)
    if winner == player_name:
        print('Bravo !!! Vous avez gagner !')
        with open('./challenges.json','r+') as json_file:
            data = json.load(json_file)
            for index, item in enumerate(data): 
                if item['name'] == challenge_name:
                    break
            else:
                index = -1

            data[index]["completed"] = True
            json_file.seek(0)
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            json_file.truncate()
        input("\nAppuyez sur Entrée pour continuer... ")
        return
    else:
        if winner:
            print(f'Le gagnant est: {winner} !')
        print('Vous avez perdu ! Voulez-vous rejouer ? (oui/non) ')
        res = input()

        if res.lower() == "oui" or res.lower() == "o":
            startChallenge(challenge_name)
        elif res.lower() == "non" or res.lower() == "n":
            print("Aurevoir ! C'était une belle partie !\n\n")
            return

        else:
            print(
                "Tu n'as pas répondu oui ni non, je vais donc me désactiver ! Aurevoir !\n\n")
            return
