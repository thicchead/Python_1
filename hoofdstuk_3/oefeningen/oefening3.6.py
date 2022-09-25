HUIDIG_JAAR = 2022
BASISPRIJS = 5

filmjaar = int(input("Jaar uitgekomen: "))
rating = int(input("Rating: "))


if HUIDIG_JAAR - filmjaar <= 2:
    BASISPRIJS += 1

if rating == 4 or rating == 5:
    BASISPRIJS += 2
elif rating == 3 or rating == 2:
    BASISPRIJS += 1

if BASISPRIJS > 7:
    BASISPRIJS = 7

print(BASISPRIJS)
