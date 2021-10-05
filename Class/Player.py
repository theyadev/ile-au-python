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
    def getName(self):
        new_name = input(f"Comment t'apelles-tu ? ")
        try:
            new_name = int(new_name)
            print('Le nom ne doit pas contenir de chiffres !\n\n')
            return self.getName()
        except:
            if (len(new_name) < 3):
                print("Le nom doit contenir plus de 2 caractères !\n\n")
                return self.getName()
            else:
                self.NAME = new_name
