def bepaal_kinderprijs(volwassenprijs, kindercode, sterren, stad):
    stad = stad[:2]
    if kindercode == "A":
        if sterren == 2 or sterren == 1:
            return 0
        if stad != "BR":
            return 0
    else:
        return volwassenprijs * 0.5


def bepaal_volwassenprijs(sterren, stad):
    stad = stad[:2]
    if stad == "HI":
        return 70
    elif sterren == 5 or sterren == 4:
        return 60
    elif sterren == 3:
        if stad == "AN" or stad == "BR":
            return 60
        else:
            return 56
    elif sterren == 2 or sterren == 1:
        return 48


def main():
    aantal_volwassenen = int(input("Aantal volwassenen: "))
    aantal_kinderen = int(input("Aantal kinderen: "))
    hotelcode = input("Hotelcode: ")

    sterren = []
    prijzen_volwassenen = []
    prijzen_kinderen = []
    totale_prijzen = []

    while hotelcode != "/":
        aantal_sterren = int(input("Aantal sterren: "))
        sterren.append(aantal_sterren)

        kindercode = input("Kindercode: ").upper
        while kindercode > 'Z' or kindercode < 'A':
            print("Foute kindercode!")
            kindercode = input("Kindercode: ").upper()

        volwassenprijs = bepaal_volwassenprijs(aantal_sterren, hotelcode)
        kinderprijs = bepaal_kinderprijs(volwassenprijs, kindercode, aantal_sterren, hotelcode)
        totale_prijs = volwassenprijs * aantal_volwassenen + kinderprijs * aantal_kinderen

        prijzen_volwassenen.append(volwassenprijs)
        prijzen_kinderen.append(kinderprijs)
        totale_prijzen.append(totale_prijs)

        hotelcode = input("Hotelcode: ")




if __name__ == '__main__':
    main()
