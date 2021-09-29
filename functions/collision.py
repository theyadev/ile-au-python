def checkChallengesCollision(challenges, x ,y):
    returning_value = ""
    for c in challenges:
        if c["completed"] == True:
            continue
        if x == c["pos"]["x"] and y == c["pos"]["y"]:
            returning_value = c["name"]
    return returning_value

def collision(x, y, p, map_mattrix):
    try:
        pos = map_mattrix[p["pos"]["y"]+y][p["pos"]["x"]+x]
        if (p["pos"]["y"]+y == -1 or p["pos"]["x"]+x == -1):
            return True
        return True if str(pos) in "1" else False
    except:
        return True