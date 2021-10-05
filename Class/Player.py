class Player:
    def __init__(self, name, x, y, seed):
        self.NAME = name
        self.POS_X = x
        self.POS_Y = y
        self.SEED = seed
    def toJson(self):
        return {
            "NAME": self.NAME,
            "POS_X": self.POS_X,
            "POS_Y": self.POS_Y,
            "SEED": self.SEED
        }
