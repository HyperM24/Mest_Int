def szamjeg_osszeg(s):
    osszeg = 0
    for c in s:
        osszeg += int(c)
        
    return osszeg

if __name__ == "__main__":
    
    s = "90146852" 
    eredmeny = szamjeg_osszeg(s)
    print(f"Számjegyek összege: {eredmeny}")