PRIJS_VOLWASSENEN = 11
PRIJS_KINDEREN = 6

aantal_volwassenen = int(input("Aantal volwassenen: "))
aantal_kinderen = int(input("Aantal kinderen: "))

print(str(aantal_volwassenen * PRIJS_VOLWASSENEN + aantal_kinderen * PRIJS_KINDEREN) + " euro")
