from random import randint
from prints import printAt
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
            printAt(2,len(texts)+7, f"Le résultat décrypté est: {TextColors.CYAN}{caesarize(text,shift)}{TextColors.RESET}")
    print(f'\033[{game_board_height};0H')

if __name__ == "__main__":
    startGame("Theya")