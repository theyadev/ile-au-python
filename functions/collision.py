from settings import *

def checkChallengesCollision(challenges, x ,y):
    returning_value = ""
    for c in challenges:
        if c["completed"] == True:
            continue
        if x == c["pos"]["x"] and y == c["pos"]["y"]:
            returning_value = c["name"]
    return returning_value

def collision(x, y):
    try:
        pos = map_mattrix[p.posY+y][p.posX+x]
        if (p.posY+y == -1 or p.posX+x == -1):
            return True
        return True if str(pos) in collision_numbers else False
    except:
        return True