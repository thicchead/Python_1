personeelsnummer = int(input("Personeelsnummer: "))

while personeelsnummer != 0:
    geslacht = int(input("Geslacht: "))

    while geslacht != 0 and geslacht != 1:
        print("Foute invoer!")
        geslacht = int(input("Geslacht: "))

    leeftijd = int(input("Leeftijd: "))
    brutoloon = float(input("Brutoloon: "))

    aantal_conditie_een = 0
    aantal_conditie_twee = 0

    if geslacht == 1:
        if leeftijd > 34:
            aantal_conditie_een += 1
        if brutoloon > 1800:
            aantal_conditie_een += 1
    else:
        if leeftijd < 25:
            aantal_conditie_twee += 1

    personeelsnummer = int(input("Personeelsnummer: "))

print(aantal_conditie_een)
print(aantal_conditie_twee)
