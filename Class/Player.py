from time import sleep
class Player:
    def __init__(self, name, x, y, seed, food = 100, stamina = 100, water = 100):
        self.NAME = name
        self.POS_X = x
        self.POS_Y = y
        self.SEED = seed
        self.FOOD = int(food)
        self.STAMINA = int(stamina)
        self.WATER = int(water)
    def toJson(self):
        return {
            "NAME": self.NAME,
            "POS_X": self.POS_X,
            "POS_Y": self.POS_Y,
            "SEED": self.SEED,
            "FOOD": self.FOOD,
            "STAMINA": self.STAMINA,
            "WATER": self.WATER
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
    def rest(self, hours):
        if self.FOOD - 2 <= 0: return False
        for i in range(round(hours)):
            self.FOOD -= 2
            if self.STAMINA + 10 > 100:
                self.STAMINA = 100
            else:
                self.STAMINA += 10
        return True
