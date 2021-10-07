from random import random
from challengesCollision import checkChallengesCollision
class Player:
    def __init__(self, name, x, y, seed, food = 100, stamina = 100, water = 100, inventory = [], map_mattrix = None, random_items = None):
        self.NAME = name
        self.POS_X = x
        self.POS_Y = y
        self.SEED = seed
        self.FOOD = int(food)
        self.STAMINA = int(stamina)
        self.WATER = int(water)
        self.INVENTORY = inventory
        self.METRIC = "kg"
        self.MAX_WEIGHT = 5
        self.MAP_MATTRIX = map_mattrix
        self.RANDOM_ITEMS = random_items
    
    def getWeight(self):
        weight = 0
        weight = sum([item.WEIGHT*item.QUANTITY for item in self.INVENTORY if item.QUANTITY > 0])
        return weight

    def getIndexItem(self, x,y):
        for index,item in enumerate(self.RANDOM_ITEMS):
            if item[1] == x and item[2] == y:
                return index 
        return False

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

    def collision(self, x, y):
        try:
            pos = self.MAP_MATTRIX[self.POS_Y+y][self.POS_X+x]
            if (self.POS_Y+y == -1 or self.POS_X+x == -1):
                return True
            
            return True if str(pos) in "124" else False
        except:
            return True

    def move(self, x, y, challenges):
        if self.STAMINA <= 0: return False
        if self.collision(x, y) == False:
            self.POS_X += x
            self.POS_Y += y
            index_item = self.getIndexItem(self.POS_X,self.POS_Y)
            if index_item and self.getWeight() < self.MAX_WEIGHT:
                self.INVENTORY[self.RANDOM_ITEMS[index_item][0]].QUANTITY += 1
                self.RANDOM_ITEMS.pop(index_item)

            self.STAMINA -= 2 if self.STAMINA > 0 else 0
            self.FOOD -= 0.05 if self.FOOD > 0 else 0
            self.WATER -= 0.25 if self.WATER > 0 else 0
            challenge = checkChallengesCollision(
                challenges, self.POS_X, self.POS_Y)
            if challenge:
                return challenge
            else:
                return False
        else:
            return False

    def rest(self, hours):
        if self.FOOD - 1 <= 0: return False
        for i in range(round(hours)):
            self.FOOD -= 1
            if self.STAMINA + 10 > 100:
                self.STAMINA = 100
            else:
                self.STAMINA += 10
        return True

    # Exports 
    
    def inventoryToJson(self):
        return [{
                "NAME": item.NAME,
                "DESC": item.DESC,
                "WEIGHT": item.WEIGHT,
                "QUANTITY": item.QUANTITY,
                "CHAR": item.CHAR
            } for item in self.INVENTORY]

    def toJson(self):
        return {
            "NAME": self.NAME,
            "POS_X": self.POS_X,
            "POS_Y": self.POS_Y,
            "SEED": self.SEED,
            "FOOD": self.FOOD,
            "STAMINA": self.STAMINA,
            "WATER": self.WATER,
            "INVENTORY": self.inventoryToJson(),
            "MAP_MATTRIX": self.MAP_MATTRIX,
            "RANDOM_ITEMS": self.RANDOM_ITEMS
        }
