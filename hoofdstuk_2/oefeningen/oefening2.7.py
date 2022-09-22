lengte_tapijt = float(input("Lengte tapijt = "))
breedte_tapijt = float(input("Breedte tapijt = "))
prijs_per_m2 = float(input("Prijs per m² = "))
plaatsingskosten_per_m2 = float(input("Plaatsingskosten per m² = "))

aantal_m2 = lengte_tapijt * breedte_tapijt
prijs_per_m2 *= aantal_m2
plaatsingskosten_per_m2 *= aantal_m2

print()
print(prijs_per_m2)
print(plaatsingskosten_per_m2)
print(prijs_per_m2 + plaatsingskosten_per_m2)
