import settings

def collision(x, y, p):
    pos = settings.M[p["pos"]["y"]+y][p["pos"]["x"]+x]
    return True if str(pos) in "12" else False