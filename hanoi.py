class Hanoi:
    def __init__(self, ke, c):
        self.ke = ke
        self.c = c

    def celtest(self, a):
        return a == self.c

    def rakovetkezo(self, a):# i = melyikre, j = hova
        gyerekek = []
        for i in range(3):
            for j in range(3):
                if i == j or not a[i]:
                    continue

                uj_allapot = [list(r) for r in a]
                ertek = uj_allapot[i][0]  # min

                if not uj_allapot[j] or ertek < uj_allapot[j][0]:
                    uj_allapot[i].pop(0)
                    uj_allapot[j].insert(0, ertek)
                    gyerekek.append(tuple(uj_allapot))
        return gyerekek


#if __name__ == "__main__":
    #eredmeny = Hanoi(([1, 2, 3], [], []), ([], [], [1, 2, 3]))

