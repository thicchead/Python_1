aantal_karakters = int(input("Aantal karakters: "))
som = 0
for i in range(aantal_karakters):
    karakter = input("Karakter: ")
    if 'a' < karakter < 'z':
        print("kleine letter")
    elif 'A' < karakter < 'Z':
        print("Hoofdletter")
    elif chr(48) <= karakter <= chr(57):
        som += int(karakter)
    else:
        print(karakter)
        print("onbekend")

print(som)

"""ord geeft een getal terug
chr geeft een letter terug"""
