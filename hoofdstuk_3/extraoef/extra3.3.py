VAST_RECHT = 25

waterverbruik = float(input("Verbruikt water = "))

meerverbruik = 0
prijs = VAST_RECHT

if waterverbruik < 30:
    prijs = prijs
elif waterverbruik < 200:
    meerverbruik = 1 * (waterverbruik - 30)
elif waterverbruik < 5000:
    meerverbruik = 1 * (waterverbruik - 30) + 1.15 * (waterverbruik - 170)
else:
    meerverbruik = 1 * (waterverbruik - 30) + 1.15 * (waterverbruik - 170) + 1.175 * (waterverbruik - 4800)

prijs += meerverbruik

print(prijs)
