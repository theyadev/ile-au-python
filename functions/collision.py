import settings

def collision(x, y, p):
    pos = settings.M[p["pos"]["y"]+y][p["pos"]["x"]+x]
    if pos != 1 and pos != 2  and pos!=3:
        return False
    else:
        return True