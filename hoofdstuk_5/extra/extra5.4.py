def bereken_korting(wagen, lid, afstand):
    basiskorting = 0
    if lid == "N":
        basiskorting = 0

    if wagen == "R":
        if lid == "J":
            basiskorting = 15
            if afstand > 10:
                basiskorting += (afstand - 10) * 1.5
    else:
        if lid == "J":
            basiskorting = 10
            if afstand > 10:
                basiskorting += (afstand - 10) * 1

    return basiskorting


def bereken_totale_kostprijs(wagen, afstand):
    if wagen == "R":
        basisprijs = 25
        if afstand > 10:
            basisprijs += (afstand - 10) * 2.25
        elif afstand > 20:
            basisprijs += (afstand - 20) * 1.75 + 22.5
    else:
        basisprijs = 20
        if afstand > 10:
            basisprijs += (afstand - 10) * 1.75
        elif afstand > 20:
            basisprijs += (afstand - 20) * 1.15 + 17.5

    return basisprijs


def main():
    naam = input("Naam: ")
    aantal = 0
    leden_mutualiteit = 0

    while naam != "/":
        soort_wagen = input("Reanimatie- of ziekenwagen: ").upper()
        afstand = int(input("Afstand in kilometer: "))
        lid_mutualiteit = input("Lid mutualiteit? ").upper()

        if lid_mutualiteit == "j".upper():
            leden_mutualiteit += 1

        totale_kostprijs = bereken_totale_kostprijs(soort_wagen, afstand)
        korting = bereken_korting(soort_wagen, lid_mutualiteit, afstand)

        print(naam + ", totale kostprijs: " + str(totale_kostprijs) + ", netto kostprijs: " + str(totale_kostprijs - korting))

        aantal += 1
        naam = input("Naam: ")

    print("Aantal slachtoffers: " + str(aantal))
    print(str(round(100 / aantal * leden_mutualiteit, 2)) + "% van de slachtoffers zijn leden van de mutualiteit")


if __name__ == '__main__':
    main()
