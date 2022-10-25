def maak_eindstring(hcode, sterren, prijs_volwassen, prijs_kind, totaal):
    eindstring = "{:<6} {:<5.2f} {:<5.2f} {:<7.2f}"
    eerste_deel = hcode.upper() + sterren * "*"
    tweede_deel = prijs_volwassen
    derde_deel = prijs_kind
    vierde_deel = totaal
    eindstring = eindstring.format(eerste_deel, tweede_deel, derde_deel, vierde_deel)

    return eindstring


def bereken_totaal(prijs_volwassen, prijs_kind, aantal_v, aantal_k):
    return aantal_v * prijs_volwassen + aantal_k * prijs_kind


def bereken_prijs_kinderen(prijs, sterren, hcode, kcode):
    hcode = hcode[:2].upper()
    if kcode == "A":
        if sterren == 1 or sterren == 2 or hcode == "BR":
            kinderprijs = 0
    else:
        kinderprijs = prijs * 0.5

    return kinderprijs


def bereken_prijs_volwassenen(sterren, hcode):
    hcode = hcode[:2].upper()

    if hcode == "HI":
        prijs = 70
    elif sterren == 5 or sterren == 4 or hcode == "BR" or hcode == "AN":
        prijs = 60
    elif sterren == 3:
        prijs = 56
    else:
        prijs = 48

    return prijs


def check_kindercode(kcode):
    juiste_code = kcode.upper()

    while juiste_code > "Z" or juiste_code < "A":
        print("Foute kindercode! ")
        juiste_code = input("Kindercode = ").upper()

    return juiste_code


def main():
    hotelcode = input("Hotelcode = ")

    while hotelcode != "/":
        aantal_volwassenen = int(input("Aantal volwassenen: "))
        aantal_kinderen = int(input("Aantal kinderen: "))
        aantal_sterren = int(input("Aantal sterren = "))

        kindercode = input("Kindercode = ")
        juiste_kindercode = check_kindercode(kindercode)

        prijs_per_persoon = bereken_prijs_volwassenen(aantal_sterren, hotelcode)
        prijs_per_kind = bereken_prijs_kinderen(prijs_per_persoon, aantal_sterren, hotelcode, juiste_kindercode)
        totale_prijs = bereken_totaal(prijs_per_persoon, prijs_per_kind, aantal_volwassenen, aantal_kinderen)

        eindstring = maak_eindstring(hotelcode, aantal_sterren, prijs_per_persoon, prijs_per_kind, totale_prijs)
        print(eindstring)

        hotelcode = input("Hotelcode = ")


if __name__ == '__main__':
    main()
