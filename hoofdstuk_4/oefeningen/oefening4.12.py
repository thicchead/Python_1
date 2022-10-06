familienaam = input("Naam: ")
totale_premie = 0

while familienaam != "/" and familienaam != "*":
    voornaam = input("Voornaam: ")
    dienstjaren = int(input("Dienstjaren: "))

    while dienstjaren < 0 or dienstjaren > 40:
        print("Teveel of te weinig!")
        dienstjaren = int(input("Dienstjaren: "))

    premie = 25 * dienstjaren

    if dienstjaren < 5:
        premie = 0

    totale_premie += premie

    hoogste_premie = 0

    if premie > hoogste_premie:
        hoogste_premie = premie

    print(familienaam)
    print(voornaam)
    print(premie)

    familienaam = input("Naam: ")

print("Hoogste premie: " + str(hoogste_premie))
print("Totale premie: " + str(totale_premie))
