def genereer_offertenummer(naam, prijs, jaar):
    prijs = str(int(prijs))

    print(str(jaar) + "_" + naam.upper() + "_" + prijs[::-1])


def bereken_prijs_poort(opp, motor, kleur):
    basisprijs = opp * 113.5 + motor
    if kleur == "JA":
        basisprijs *= 1.10

    return basisprijs


def bereken_motorprijs(motor):
    if motor == "A101":
        return 120
    elif motor == "A105":
        return 220.5
    else:
        return 250.5


def bepaal_motor(gew):
    if gew < 150:
        return "A101"
    elif gew <= 300:
        return "A105"
    else:
        return "X300"


def bereken_gewicht(opp):
    return opp * 11


def bereken_oppervlakte(h, b):
    return h * b


def maak_breedte():
    breedte = float(input("Breedte: "))

    while breedte > 8 or breedte < 2:
        print("Foute breedte!")
        breedte = float(input("Breedte: "))

    return breedte


def maak_hoogte():
    hoogte = float(input("Hoogte: "))

    while hoogte > 6.5 or hoogte < 2:
        print("Foute hoogte!")
        hoogte = float(input("Hoogte: "))

    return hoogte


def main():
    verkoper = input("Naam: ")
    hoogte = maak_hoogte()
    breedte = maak_breedte()
    kleur = input("Speciale kleur? ").upper()

    oppervlakte = bereken_oppervlakte(hoogte, breedte)
    gewicht = bereken_gewicht(oppervlakte)

    motornaam = bepaal_motor(gewicht)
    motorprijs = bereken_motorprijs(motornaam)

    prijs_poort = bereken_prijs_poort(oppervlakte, motorprijs, kleur)
    jaar = 2022
    genereer_offertenummer(verkoper, prijs_poort, jaar)


if __name__ == '__main__':
    main()
