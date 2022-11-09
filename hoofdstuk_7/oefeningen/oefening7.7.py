def bepaal_tijd(totale_tijd):  # 60 minuten is een uur erbij doen
    """uren = tijd // 3600
    rest = tijd % 3600
    minuten = rest // 60
    seconden = rest % 60"""
    totale_tijd = int(totale_tijd)
    aantal_uren = totale_tijd // 3600
    aantal_minuten = (totale_tijd - 3600 * aantal_uren) // 60
    aantal_seconden = totale_tijd - 3600 * aantal_uren - 60 * aantal_uren
    if aantal_seconden >= 30:
        aantal_minuten += 1

    return str(aantal_uren) + "u " + str(aantal_minuten) + "m"


def bepaal_leeftijd(gebdatum):
    vandaag = [7, 11, 2022]
    verjaardag = gebdatum.split("/")

    for i in range(len(verjaardag)):
        verjaardag[i] = int(verjaardag[i])

    leeftijd = vandaag[-1] - verjaardag[-1]
    if vandaag[-2] < verjaardag[-2]:
        leeftijd -= 1

    if vandaag[-2] == verjaardag[-2]:
        if vandaag[-3] < verjaardag[-3]:
            leeftijd -= 1

    return leeftijd


def bepaal_punten(juist, antwoorden_gebruiker):
    punten = 20

    antwoorden = []
    for antwoord in antwoorden_gebruiker:
        antwoorden.append(antwoord)

    juiste_antwoorden = []
    for antwoord in juist:
        juiste_antwoorden.append(antwoord)

    for i in range(len(antwoorden)):
        if antwoorden[i] == juiste_antwoorden[i]:
            punten += 2
        elif antwoorden[i] != "E":
            punten -= 1

    return punten


def main():
    juiste_antwoorden = input("Juiste antwoorden: ").upper()
    deelnemer_gegevens = input("Gegevens deelnemer: ").upper()

    deelnemersnummers = []
    geboortedatumlijst = []
    antwoordenlijst = []
    tijd_in_sec = []
    puntenlijst = []

    aantal = 0

    while deelnemer_gegevens != "0":
        gegevenslijst = deelnemer_gegevens.split(" ")
        nummer = gegevenslijst[0]
        geboortedatum = gegevenslijst[1]
        antwoorden = gegevenslijst[2]
        tijd = gegevenslijst[3]

        deelnemersnummers.append(nummer)
        geboortedatumlijst.append(bepaal_leeftijd(geboortedatum))
        antwoordenlijst.append(antwoorden)
        tijd_in_sec.append(bepaal_tijd(tijd))
        puntenlijst.append(bepaal_punten(juiste_antwoorden, antwoorden))

        aantal += 1

        deelnemer_gegevens = input("Gegevens deelnemer: ").upper()

    """huge arrays on top, append bij elke invoer, op het einde een for loop met
    formatting, en huge_array[i] op de juiste plaats zetten dan"""

    for i in range(aantal):
        print(str(i + 1) + '. {} {} jaar {} {} ptn'.format(str(deelnemersnummers[i]), str(geboortedatumlijst[i]), str(tijd_in_sec[i]), str(puntenlijst[i])))


if __name__ == '__main__':
    main()
