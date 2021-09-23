def getName():
    n = input(f"Comment t'apelles-tu ? ")
    try:
        n = int(n)
        print('Le nom ne doit pas contenir de chiffres !\n\n')
        return getName()
    except:
        if (len(n) < 3):
            print("Le nom doit contenir plus de 2 caractères !\n\n")
            return getName()
        else:
            return n