naam = input("Naam speleer: ")
prijs_vorig_seizoen = int(input("Prijs vorig seizoen: "))
leeftijd = int(input("Leeftijd: "))
beoordelingscijfer = float(input("Beoordelingscijfer: "))
type_speler = input("Type speler: ")
aantal_doelpunten = int(input("Aantal doelpunten: "))

BASISPRIJS = prijs_vorig_seizoen

if leeftijd < 25:
    BASISPRIJS *= 1.10
elif leeftijd > 30:
    BASISPRIJS *= 0.95

if type_speler == "aanvaller":
    if aantal_doelpunten > 5:
        BASISPRIJS += (aantal_doelpunten - 5) * 20000 + 50000
    else:
        BASISPRIJS += aantal_doelpunten * 10000
elif type_speler == "middenvelder" or type_speler == "verdediger" or type_speler == "doelman":
    BASISPRIJS += 10000 * beoordelingscijfer
    if type_speler == "doelman":
        if aantal_doelpunten > 20:
            BASISPRIJS -= 9000

print(naam)
print(prijs_vorig_seizoen)
print(BASISPRIJS)
