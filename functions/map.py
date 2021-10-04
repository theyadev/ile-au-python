from settings import initChallenges
from collision import checkChallengesCollision
from Colors import *

'''
0 = Terrain
1 = Caillasse
2 = L'eau
3 = Foret
4 = Sable
5 = Defi
'''

format_prefix = "\033["
position_suffix = "H"


def printAt(x, y, text, size):
    print(f"{format_prefix}{y};{x+size}{position_suffix}{text}")


def printMap(settings, p):
    map_mattrix = settings['map']
    challenges = initChallenges()
    print(f"Partie de Theya !")
    for y in range(len(map_mattrix)):
        for x in range(len(map_mattrix[y])):
            map_elem = map_mattrix[y][x]
            back_color = ""
            txt_color = ""
            txt = " "
            if checkChallengesCollision(challenges, x, y):
                # TODO: X Rouge
                txt_color = TextColors.RED
                txt = "X"
            elif map_elem == 1:
                # TODO: BG Gris
                back_color = BackgroundColors.WHITE
            elif map_elem == 2:
                # TODO: BG Bleu
                back_color = BackgroundColors.CYAN
            elif map_elem == 3:
                # TODO: f Vert
                txt_color = TextColors.GREEN
                txt = "f"
            elif map_elem == 4:
                # TODO: petit char vert aussi
                txt_color = TextColors.GREEN
                txt = "F"
            elif map_elem == 5:
                # TODO: BG Jaune
                back_color = BackgroundColors.YELLOW
            if x == p['pos']['x'] and y == p['pos']['y']:
                txt_color = TextColors.WHITE
                txt = "a"
            printAt(x+2, y+2, f'{back_color}{txt_color}{txt}{TextColors.RESET}{BackgroundColors.RESET}', 2)
    print('Haut: "z", Gauche: "q", Bas: "s", Droite:"d" | Inventaire: "e" | Quitter: "l"')
    print(f'Position Y: {p["pos"]["y"]} | Position X: {p["pos"]["x"]}')
