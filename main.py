import settings
import sys

sys.path.append('./functions/')

from clear import cls
from getName import getName
from map import printMap
from userInput import userInput

settings.init()

def init():
    p = {
        "name": getName(),
        "pos": {
            "x": settings.m-settings.m//25-1,
            "y": settings.n-settings.n//15-1
        }
    }

    printMap(p)
    userInput(p)


if __name__ == '__main__':
    init()
