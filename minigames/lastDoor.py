from settings import p

def startGame(player_name):
    required_items = [3,4,5]
    for item_id in required_items:
        for item in p.INVENTORY:
            if item.ID == item_id:
                if item.QUANTITY == 0:
                    return False
                else:
                    item.QUANTITY -= 1
    return player_name
