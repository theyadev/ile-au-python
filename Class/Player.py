class Player:
    def __init__(self, name, x, y, seed):
        self.name = name
        self.posX = x
        self.posY = y
        self.seed = seed
    def toJson(self):
        return {
            "name": self.name,
            "posX": self.posX,
            "posY": self.posY,
            "seed": self.seed
        }
