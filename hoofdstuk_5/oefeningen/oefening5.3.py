HUIDIG_JAAR = 2022


def bereken_lidgeld(lt, kinderen, inkomen, jaar):
    aanvangsgeld = 100

    if lt > 60:
        aanvangsgeld -= 15

    vermindering_kinderen = 7.5 * kinderen
    if vermindering_kinderen > 35:
        vermindering_kinderen = 35

    aanvangsgeld -= vermindering_kinderen

    aantal_jaren_lid = HUIDIG_JAAR - jaar

    if aantal_jaren_lid > 20:
        aanvangsgeld -= 12.5

    if inkomen < 7500:
        aanvangsgeld -= 25

    if aanvangsgeld < 50:
        aanvangsgeld = 50

    return aanvangsgeld


def main():
    naam = input("Naam: ")

    while naam != "x" and naam != "X":
        leeftijd = int(input("Leeftijd: "))
        aantal_kinderen = int(input("Aantal kinderen: "))
        inkomen = int(input("Inkomen: "))
        aansluitingsjaar = int(input("Aansluitingsjaar: "))

        print(bereken_lidgeld(leeftijd, aantal_kinderen, inkomen, aansluitingsjaar))

        naam = input("Naam: ")


if __name__ == '__main__':
    main()
