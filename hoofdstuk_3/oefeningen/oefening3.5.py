EENHEIDSPRIJS = 11.5
BTWPERCENTAGE = 0.21

aantal_artikels = int(input("Aantal artikelen die je wilt bestellen: "))

totale_prijs = EENHEIDSPRIJS * aantal_artikels * (1 + BTWPERCENTAGE)

if totale_prijs > 1000:
    totale_prijs *= 0.90

print(totale_prijs)
