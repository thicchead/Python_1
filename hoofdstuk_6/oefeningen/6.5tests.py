def bereken_prijs_kinderen(prijs, sterren, hcode, kcode):
    hcode = hcode[:2].upper()
    if kcode == "A":
        if sterren == 1 or sterren == 2 or hcode == "BR":
            kinderprijs = 0
    else:
        kinderprijs = prijs * 0.5

    return kinderprijs


# def check_code(kcode):
#     juist = kcode
#     while juist > "Z" or juist < "A" or len(juist) != 1:
#         print("Foute kindercode! ")
#         juist = input("Kindercode = ").upper()
#
#     return juist


def main():
    volwassenprijs = 60
    aantal_sterren = 5
    hotelcode = "BR1234"
    kindercode = "B"

    oehoeh = bereken_prijs_kinderen(volwassenprijs, aantal_sterren, hotelcode, kindercode)
    print(oehoeh)
    # hotelcode = "br1234"
    # print(hotelcode[:2].upper())
    # kindercode = input("Kindercode: ").upper()
    # juiste_code = check_code(kindercode)
    #
    # print(juiste_code)


if __name__ == '__main__':
    main()
