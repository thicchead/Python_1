BOETEBEDRAG = 0.07


def bereken_boete(boeken, dagen):
    boete = boeken * dagen * BOETEBEDRAG

    for i in range(1, dagen + 1):
        if i % 45 == 0:
            boete += 0.84
    # if dagen >= 45:
    #     boete += 0.84

    return boete


def bereken_brieven(dagen):
    aantal_brieven = 0

    for i in range(1, dagen + 1):
        if i % 45 == 0:
            aantal_brieven += 1

    return aantal_brieven


def main():
    naam = input("Naam: ")
    totaal_aantal_dagen = 0
    # teller = 0

    while naam != "xx":
        aantal_boeken = int(input("Aantal boeken: "))
        aantal_dagen_overschreden = int(input("Aantal dagen overschreden: "))

        totaal_aantal_dagen += aantal_dagen_overschreden
        # if aantal_dagen_overschreden >= 45:
        #     teller += 1

        print(bereken_boete(aantal_boeken, aantal_dagen_overschreden))

        naam = input("Naam: ")

    print(bereken_brieven(totaal_aantal_dagen))
    # print(teller)


if __name__ == '__main__':
    main()
