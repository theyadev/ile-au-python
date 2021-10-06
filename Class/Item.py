class Item:
    def __init__(self, name, description, weight, quantity, char):
        self.NAME = name
        self.DESC = description
        self.WEIGHT = weight
        self.QUANTITY = quantity
        self.CHAR = char
    
    def remove(self, nb):
        if self.QUANTITY - nb < 0: return
        self.QUANTITY -= nb
    
    def add(self, nb):
        self.QUANTITY += nb