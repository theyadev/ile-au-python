from random import randint
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

texts = ["Beautiful is better than ugly.",
"Explicit is better than implicit.",
"Simple is better than complex."]
def startGame(player_name):
    letter_shift = "wswcqsd"
    while len(letter_shift) > 1 or letter_shift.isnumeric():
        letter_shift = input("Entrez une lettre: ")
    shift = ord(letter_shift) -  ord('a') if len(letter_shift)>0 else 0
    for i in range(5):
        text = input("Entrez du texte: ")
        if caesarize(text,shift).lower() == player_name.lower():
            return player_name
        elif len(text)==1:
            print(caesarize(text,shift))

if __name__ == "__main__":
    startGame("Theya")