aantal_sterren = int(input("Aantal sterren = "))
code = input("Code = ")
aantal_overnachtingen = int(input("Aantal overnachtingen = "))
seizoen = input("Seizoen = ")

prijs_per_nacht = 0
if aantal_sterren == 1:
    prijs_per_nacht = 30
elif aantal_sterren == 2 or aantal_sterren == 3:
    prijs_per_nacht = 40
else:
    prijs_per_nacht = 55

overnachtingskosten = prijs_per_nacht * aantal_overnachtingen

maaltijdkosten = 0
if code == "O":
    maaltijdkosten = overnachtingskosten * 0.2
elif code == "H":
    maaltijdkosten = overnachtingskosten * 0.5
elif code == "V":
    maaltijdkosten = overnachtingskosten * 0.6
else:
    maaltijdkosten = overnachtingskosten * 0.6 + 80 * aantal_overnachtingen

totale_prijs = overnachtingskosten + maaltijdkosten

if seizoen == "L" and (code == "O" or code == "H"):
    totale_prijs *= 0.9

print("Prijs voor 1 persoon: " + str(totale_prijs))
