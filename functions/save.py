import json


def save(p):
    with open('./player.json', 'w') as json_file:
        json.dump(p.toJson(), json_file, ensure_ascii=False, indent=4)
    return
