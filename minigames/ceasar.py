from random import randint
from prints import printAt, printAnimation
from Colors import TextColors
from settings import *

def caesarize_letter(letter, shift):
    if 'A' <= letter.upper() <= 'Z':
        start = ord('a') if letter.islower() else ord('A')
        return chr((ord(letter) - start + shift) % 26 + start)
    else:
        return letter

def caesarize(text, shift):
    return ''.join([caesarize_letter(letter, shift) for letter in text])

def uncaesarize(text, shift):
    return ''.join([caesarize_letter(letter, -1 * shift) for letter in text])

texts = [f"Beautiful is better than ugly.",
f"Explicit is better than implicit.",
f"Simple is better than complex."]

game_board_height = 12
game_board_width = 100

def printGameBoard():
    for y in range(game_board_height):
        for x in range(game_board_width):
            if y == 1:
                if x == 1:
                    printAt(x, y, up_left)
                elif x == game_board_width-1:
                    printAt(x, y, up_right)
                else:
                    printAt(x, y, horizontal)
            elif y == 5:
                if x == 1:
                    printAt(x, y, vert_right)
                elif x == game_board_width-1:
                    printAt(x, y, vert_left)
                else:
                    printAt(x, y, horizontal)
            elif y == 8:
                if x == 1:
                    printAt(x, y, vert_right)
                elif x == game_board_width-1:
                    printAt(x, y, vert_left)
                else:
                    printAt(x, y, horizontal)
            elif y == game_board_height-1:
                if x == 1:
                    printAt(x, y, bot_left)
                elif x == game_board_width-1:
                    printAt(x, y, bot_right)
                else:
                    printAt(x, y, horizontal)
            else:
                if x == 0 or x == game_board_width-1:
                    printAt(x, y, vertical)

def startGame(player_name):
    clear()
    textContinue = '\nAppuyez sur entr??e pour continuer...'
    texts_history = ["Au nord de la plage, tu trouves un petit temple taill?? dans la paroi rocheuse. Au-dessus de l???arche d???entr??e, est ??crit un message dans une langue apparemment inconnue mais utilisant l???alphabet habituel.\n\n",
             "Sur les colonnes de l???arche, sont d???ailleurs grav??es en relief toutes les lettres de l???alphabet. Curieux, tu appuies au hasard sur l???une des lettres et tu t???aper??ois que les lettres formant le message changent. Malgr?? cela, le message en lui-m??me reste incompr??hensible. En effectuant plusieurs tests, tu te rends compte qu???a une lettre d??finie correspond une composition sp??cifique du message. Ne voyant pas trop quoi faire d???autre pour le moment, tu d??cides d???entrer dans le temple.\n\n",
             f"\033[23mBonjour explorateur ! Pour ouvrir la porte de la montagne, atteindre le c??ur de l?????le et rejoindre tes compagnons, tu devras tout d???abord prouver ta valeur individuelle en gagnant les 3 cl??s que tu obtiendras en relevant les d??fis appropri??s. Ceci est le premier d???entre eux\033[0m\n\n",
             "?? l???int??rieur, tout le sol est recouvert de sable. Au milieu de la petite pi??ce, se trouve un autel avec une niche ferm??e par une grille apparemment sans serrure. ?? l???int??rieur de la niche tu vois une grosse cl?? en argent (inatteignable tant que la grille est en place). ?? c??t?? de la niche, un ??criteau en bois indique : ?? R??cite le cr??do du Python, puis trace ton nom secret ??.\n\n",
    ]

    for text in texts_history:
       printAnimation(text)
    input(textContinue)
    clear()
    for i, text in enumerate(texts): printAt(2, i+2, f"{TextColors.RED if i == 0 else TextColors.GREEN if i == 1 else TextColors.BLUE}{text.center(98)}{TextColors.RESET}")
    printGameBoard()
    letter_shift = "wswcqsd"
    while len(letter_shift) > 1 or letter_shift.isnumeric():
        enter_text = "Veuillez entrer une lettre ci dessous."
        printAt(2, len(texts)+3, f"{enter_text} {' '*(game_board_width-len(enter_text)-5)}")
        printAt(2, len(texts)+4, " "*(game_board_width-5))
        letter_shift = input(f"\033[{len(texts)+4};2HLettre: ")
    shift = ord(letter_shift) -  ord('a') if len(letter_shift) > 0 else 0

    for i, text in enumerate(texts): printAt(2, i+2, f"{TextColors.RED if i == 0 else TextColors.GREEN if i == 1 else TextColors.BLUE}{caesarize(text.center(98), shift)}{TextColors.RESET}")
    printGameBoard()
    

    for i in range(5):
        printAt(2, len(texts)+6, " "*(game_board_width-5))
        text = input(f"\033[{len(texts)+6};2HEntrez du texte: ")
        if caesarize(text,shift).lower() == player_name.lower():
            print(f'\033[{game_board_height};0H')
            return player_name
        else:
            printAt(2, len(texts)+7, " "*(game_board_width-5))
            printAt(2,len(texts)+7, f"Le r??sultat d??crypt?? est: {TextColors.CYAN}{caesarize(text,shift)}{TextColors.RESET}")
    print(f'\033[{game_board_height};0H')

if __name__ == "__main__":
    startGame("Theya")