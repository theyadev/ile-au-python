import numpy as np

def init():
    global n, m, M
    n, m = 30, 50
    M = np.zeros((n, m))

    # Cailloui
    M[0:(n//15), :] = 1
    M[0:int(2./3*n), 0:(m//25)] = 1
    M[0:int(2./3*n), m-m//25:m] = 1

    # O
    M[int(2./3*n):, 0:(m//25)] = 2
    M[int(2./3*n):, m-m//25:m] = 2
    M[n-(n//15):n, :] = 2

    # riviairt
    pourcentage = 0.5
    M[(n//15): int(1./3*n),      int(1./3*n):(int(1./3*n)+(m//25))] = 2
    M[(int(1./3*n)-n//30): (int(1./3*n)+n//15-n//30), (int(1./3*n)+(n//15)-m//50): int(pourcentage*m)-m//50] = 2
    M[(int(1./3*n)+n//15-n//15):, int(pourcentage*m)-m//25: int(pourcentage*m)] = 2


    # test
    M[25, 45] = 5
    M[12, 34] = 5