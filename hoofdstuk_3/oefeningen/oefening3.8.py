afstand_vlucht = float(input("Afstand van je vlucht: "))
klasse = int(input("Klasse = "))

if afstand_vlucht < 1000:
    prijs_vlucht = 0.25 * afstand_vlucht
elif afstand_vlucht < 2999:
    prijs_vlucht = 0.2 * afstand_vlucht
else:
    prijs_vlucht = 0.12 * afstand_vlucht

if klasse == 3:
    prijs_vlucht *= 1.3
elif klasse == 2:
    prijs_vlucht *= 0.8

print(prijs_vlucht)
