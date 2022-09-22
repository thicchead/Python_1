afgelegde_km = float(input("Aantal afgelegde km per jaar = "))
verbruik = float(input("Verbruik (in liter) = "))
prijs_per_liter = float(input("Prijs 1 liter = "))

totale_kosten = (afgelegde_km / 100) * (verbruik / 1 * prijs_per_liter)
kostprijs_per_km = verbruik / 100 * prijs_per_liter

print(totale_kosten)
print(kostprijs_per_km)
