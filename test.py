class Kancsok:
    def __init__(self, kezdo: tuple, cel: int):
        self.kezdo = kezdo
        self.cel = cel
        self.max1 = 3
        self.max2 = 5
        self.max3 = 8

    def celteszt(self, a: tuple):  # a = (a1,a2,a3) állapot
        return a[0] == self.cel or a[1] == self.cel or a[2] == self.cel

    def rakovetkezo(self, a: tuple):
        gyerekek = []
        a1, a2, a3 = a

        # tölt 1,2
        if a1 != 0 and a2 != self.max2:
            T = min(a1, self.max2 - a2)
            gyerekek.append(("tölt 1-ből 2-be", (a1 - T, a2 + T, a3)))

        # tölt 1,3
        if a1 != 0 and a3 != self.max3:
            T = min(a1, self.max3 - a3)
            gyerekek.append(("tölt 1-ből 3-ba", (a1 - T, a2, a3 + T)))

        # tölt 2,1
        if a2 != 0 and a1 != self.max1:
            T = min(a2, self.max1 - a1)
            gyerekek.append(("tölt 2-ből 1-be", (a1 + T, a2 - T, a3)))

        # tölt 2,3
        if a2 != 0 and a3 != self.max3:
            T = min(a2, self.max3 - a3)
            gyerekek.append(("tölt 2-ből 3-ba", (a1, a2 - T, a3 + T)))

        # tölt 3,1
        if a3 != 0 and a1 != self.max1:
            T = min(a3, self.max1 - a1)
            gyerekek.append(("tölt 3-bol 1-be", (a1 + T, a2, a3 - T)))

        # tölt 3,2
        if a3 != 0 and a2 != self.max2:
            T = min(a3, self.max2 - a2)
            gyerekek.append(("tölt 3-bol 2-be", (a1, a2 + T, a3 - T)))

        return gyerekek
    


def main():
    # Létrehozzuk a feladatot
    feladat = Kancsok((0, 0, 8), 4)

    # Itt tartunk éppen a töltögetésben
    jelenlegi_allapot = feladat.kezdo
    
    # Egy egyszerű lista, amiben gyűjtjük, milyen állapotokban jártunk már
    voltunk_mar_itt = []
    voltunk_mar_itt.append(jelenlegi_allapot)

    # Addig megyünk, amíg a célteszt nem lesz igaz (azaz amíg nincs meg a 4 liter)
    while feladat.celteszt(jelenlegi_allapot) == False:
        
        # Lekérjük a lehetséges lépéseket az adott állapotból
        lehetseges_lepesek = feladat.rakovetkezo(jelenlegi_allapot)

        # Végigmegyünk az összes kapott lehetőségen
        for lepes in lehetseges_lepesek:
            # A lépés egy páros, szétszedjük egy szövegre és egy új állapotra
            szoveg = lepes[0]
            uj_allapot = lepes[1]

            # Ha ezt az új állapotot még nem vizsgáltuk korábban
            if uj_allapot not in voltunk_mar_itt:
                jelenlegi_allapot = uj_allapot
                voltunk_mar_itt.append(uj_allapot)
                print(szoveg, "->", jelenlegi_allapot)
                
                # Megtaláltuk a következő jó lépést, így kilépünk a for ciklusból
                break

    print("Megoldas: ", jelenlegi_allapot)

if __name__ == "__main__":
    main()