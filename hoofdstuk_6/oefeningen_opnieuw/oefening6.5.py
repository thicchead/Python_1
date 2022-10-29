def maak_eindstring(hcode, sterren, volwassenprijs, kinderprijs, totaalprijs):
    outputstring = "{0:} {1:.2f} {2:.2f} {3:.2f}"

    print(outputstring.format(hcode + str(sterren * "*"), volwassenprijs, kinderprijs, totaalprijs), end=" ")


def bereken_prijs_per_kind(volwassenprijs, sterren, stad, code):
    if code == "A":
        if sterren == 2 or sterren == 1:
            return 0
        elif stad != "BR":
            return 0
    else:
        return volwassenprijs * 0.5


def bereken_prijs_per_volwassene(sterren, stad):
    if stad == "HI":
        return 70
    elif sterren == 5 or sterren == 4:
        return 60
    elif sterren == 3:
        if stad == "BR" or stad == "AN":
            return 60
        else:
            return 56
    elif sterren == 2 or sterren == 1:
        return 48


def check_kindercode():
    code = input("Kindercode: ").upper()

    while code > "Z" or code < "A":
        print("Foute kindercode!")
        code = input("Kindercode: ")

    return code


def main():
    aantal_volwassenen = int(input("Aantal volwassenen = "))
    aantal_kinderen = int(input("Aantal kinderen = "))

    hotelcode = input("Hotelcode = ").upper()
    stadscode = hotelcode[:2]

    while hotelcode != "/":
        aantal_sterren = int(input("Aantal sterren = "))
        kindercode = check_kindercode()

        prijs_per_persoon = float(bereken_prijs_per_volwassene(aantal_sterren, stadscode))

        prijs_per_kind = float(bereken_prijs_per_kind(prijs_per_persoon, aantal_sterren, stadscode, kindercode))

        totale_prijs = float(aantal_volwassenen * prijs_per_persoon + aantal_kinderen * prijs_per_kind)

        maak_eindstring(hotelcode, aantal_sterren, prijs_per_persoon, prijs_per_kind, totale_prijs)

        hotelcode = input("Hotelcode = ")
        stadscode = hotelcode[:2].upper()


if __name__ == '__main__':
    main()
