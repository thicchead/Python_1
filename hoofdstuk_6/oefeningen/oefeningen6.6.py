HUIDIG_JAAR = 2022


def genereer_offertenummer(jaar, nm, prijs):
    prijs = str(int(prijs))
    prijs = prijs[::-1]

    offertenummer = str(jaar) + "_" + nm.upper() + "_" + prijs

    return offertenummer


def bereken_totaal(opp, motor, kleur):
    basisprijs = opp * 113.5 + motor

    if kleur == "J":
        basisprijs *= 1.10

    totaalprijs = basisprijs + motor

    return totaalprijs


def bereken_motorprijs(mot):
    if mot == "X300":
        prijs = 250.5
    elif mot == "A105":
        prijs = 220.5
    else:
        prijs = 120

    return prijs


def bepaal_motor(gew):
    if gew > 300:
        motor = "X300"
    elif gew > 150:
        motor = "A105"
    else:
        motor = "A101"

    return motor


def bereken_gewicht(opp):
    return 11 * opp


def bereken_oppervlakte(h, b):
    return h * b


def check_breedte(b):
    while b < 2 or b > 8:
        print("Foute breedte ingegeven!")
        b = float(input("Breedte: "))

    return b


def check_hoogte(h):
    while h < 2.5 or h > 6.5:
        print("Foute hoogte ingegeven!")
        h = float(input("Hoogte: "))

    return h


def main():
    naam = input("Naam verkoper: ")

    hoogte = float(input("Hoogte: "))
    juiste_hoogte = check_hoogte(hoogte)
    # print(hoogte)
    # print(juiste_hoogte)
    breedte = float(input("Breedte: "))
    juiste_breedte = check_breedte(breedte)
    # print(breedte)
    # print(juiste_breedte)
    oppervlakte = bereken_oppervlakte(juiste_hoogte, juiste_breedte)
    gewicht = bereken_gewicht(oppervlakte)
    print(gewicht)
    motor = bepaal_motor(gewicht)
    prijs_motor = bereken_motorprijs(motor)
    kleurkeuze = input("Speciale kleur (J/N)? ").upper()

    prijs_poort = bereken_totaal(oppervlakte, prijs_motor, kleurkeuze)
    print(prijs_poort)

    offertenummer = genereer_offertenummer(HUIDIG_JAAR, naam, prijs_poort)

    print(offertenummer)


if __name__ == '__main__':
    main()
