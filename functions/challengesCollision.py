from settings import *

def checkChallengesCollision(challenges, x ,y):
    returning_value = ""
    for c in challenges:
        if c["completed"] == True:
            continue
        if x == c["pos"]["x"] and y == c["pos"]["y"]:
            returning_value = c
    return returning_value