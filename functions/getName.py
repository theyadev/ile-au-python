def getName():
    n = input(f"Quel est ton pseudonyme ?")
    try:
        n = int(n)
        print('Nom invalide.\n\n')
        return getName()
    except:
        return n