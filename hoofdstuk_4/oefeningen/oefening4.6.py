artikelnummer = int(input("Artikelnummer = "))

totaal = 0

while artikelnummer != 999:
    hoeveelheid = int(input("Hoeveelheid = "))
    eenheidsprijs = int(input("Eenheidsprijs = "))

    print(artikelnummer)
    print(hoeveelheid)
    print(eenheidsprijs)

    totaal += hoeveelheid * eenheidsprijs

    artikelnummer = int(input("Artikelnummer = "))

print(totaal)
