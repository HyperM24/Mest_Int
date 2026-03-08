import numpy as np


class Kiralynok:
    def __init__(self, ke, c):
        self.kezdo = ke 
        self.cel = c  
        self.n = len(ke[0])  

    def celteszt(self, a):
        
        return a[1] == self.n

    def rakovetkezo(self, t):
        gyerekek = []
        s = t[1]  
        a = t[0].copy()

        for i in range(self.n):
            elofeltetel = True

           
            for sor in range(s):
                if a[sor, i] == 1:
                    elofeltetel = False
                    break

            
            if elofeltetel:
                for sor in range(s):
                    for oszlop in range(self.n):
                        if a[sor, oszlop] == 1 and abs(s - sor) == abs(i - oszlop):
                            elofeltetel = False
                            break
                    if not elofeltetel:
                        break

            if elofeltetel:
                uj_allpot = a.copy()
                uj_allpot[s, i] = 1
                gyerekek.append((uj_allpot, s + 1))

        return gyerekek


def main():
    tabla = np.zeros((8, 8), dtype=int)
    feladat = Kiralynok((tabla, 0), 8)  

    allapotok = [feladat.kezdo]

    while allapotok:
        uj_allapot = []
        for a in allapotok:
            if feladat.celteszt(a):
                print(a[0])
                return
            uj_allapot += feladat.rakovetkezo(a)
        allapotok = uj_allapot


if __name__ == "__main__":
    main()