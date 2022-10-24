def bepaal_totaal(volwassenen, volwassenprijs, kinderen, kinderprijs):
    return volwassenprijs * volwassenen + kinderprijs * kinderen


def bepaal_prijs_kinderen(kcode, prijs_volwassenen, sterren, code):
    prijs_per_kind = 0
    if kcode == "A":
        if sterren == 1 or sterren == 2 or code != "BR":
            prijs_per_kind = 0
    else:
        prijs_per_kind = prijs_volwassenen * 0.5

    return prijs_per_kind


def bepaal_prijs_volwassenen(code, sterren):

    if code == "HI":
        prijs_per_volwassene = 70
    elif sterren == 5 or sterren == 4:
        prijs_per_volwassene = 60
    elif sterren == 3:
        prijs_per_volwassene = 56
        if code == "BR" or code == "AN":
            prijs_per_volwassene = 60
    else:
        prijs_per_volwassene = 48

    return prijs_per_volwassene


def main():
    aantal_volwassenen = int(input("Aantal volwassenen: "))
    aantal_kinderen = int(input("Aantal kinderen: "))
    hotelcode = input("Hotelcode: ")
    code = hotelcode[:2].upper()

    while hotelcode != "/":
        aantal_sterren = int(input("Aantal sterren: "))
        kindercode = input("Kindercode: ")

        while kindercode.upper() > "Z" or kindercode.upper() < "A":
            kindercode = input("Kindercode: ")

        volwassenprijs = bepaal_prijs_volwassenen(code, aantal_sterren)
        kinderprijs = bepaal_prijs_kinderen(kindercode.upper(), volwassenprijs, aantal_sterren, code)
        totaalprijs = bepaal_totaal(aantal_volwassenen, volwassenprijs, aantal_kinderen, kinderprijs)

        hotelcode = input("Hotelcode: ")

    eindstring = "{:<6}{:<5} {:<5.2f} {:<5.2f} {:<7.2f}"
    print(eindstring.format(hotelcode.upper(), aantal_sterren * "*", volwassenprijs, kinderprijs, totaalprijs))


if __name__ == '__main__':
    main()
