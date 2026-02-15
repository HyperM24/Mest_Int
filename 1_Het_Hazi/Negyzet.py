def negyzetosszeg(n):
    osszeg = 0
    
    for i in range(1, n + 1):
        osszeg += i * i
    return osszeg

def osszegnegyzet(n):
    osszeg = 0
    for i in range(1, n + 1):
        osszeg += i
    return osszeg * osszeg


if __name__ == "__main__":

    n = 100
    negyossz = negyzetosszeg(n)
    ossznegy = osszegnegyzet(n)
    kulonbseg = ossznegy - negyossz

    print(f"A négyzetösszeg: {negyossz}")
    print(f"A Összeg négyzete: {ossznegy}")
    print(f"A különbség: {kulonbseg}")