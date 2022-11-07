def print_finale_lijst(gegevens, juiste_ant, aantal_deelnemers):
    deelnemersnummer = gegevens[0]
    leeftijd = bepaal_leeftijd(gegevens)
    tijd = bepaal_tijd(gegevens)
    punten = bepaal_punten(juiste_ant, gegevens)

    for i in range(aantal_deelnemers):
        print(str(aantal_deelnemers) + ". " + str(deelnemersnummer) + " " + str(leeftijd) + " jaar " + str(tijd) + " " + str(punten) + " ptn")


def bepaal_tijd(gegevens):  # 60 minuten is een uur erbij doen
    aantal_seconden = int(gegevens[3])
    """uren = tijd // 3600
    rest = tijd % 3600
    minuten = rest // 60
    seconden = rest % 60"""
    aantal_uren = aantal_seconden // 3600
    aantal_minuten = (aantal_seconden - 3600 * aantal_uren) // 60
    aantal_seconden = aantal_seconden - 3600 * aantal_uren - 60 * aantal_uren
    if aantal_seconden >= 30:
        aantal_minuten += 1

    return str(aantal_uren) + "u " + str(aantal_minuten) + "m"


def bepaal_leeftijd(gegevens):
    vandaag = [7, 11, 2022]
    geboortedatum = gegevens[1].split("/")

    for i in range(len(geboortedatum)):
        geboortedatum[i] = int(geboortedatum[i])

    leeftijd = vandaag[-1] - geboortedatum[-1]
    if vandaag[-2] < geboortedatum[-2]:
        leeftijd -= 1

    if vandaag[-2] == geboortedatum[-2]:
        if vandaag[-3] < geboortedatum[-3]:
            leeftijd -= 1

    return leeftijd


def bepaal_punten(juist, gegevens):
    punten = 20
    deelnemer_antwoord = gegevens[2]

    antwoorden = []
    for antwoord in deelnemer_antwoord:
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

    aantal = 0

    while deelnemer_gegevens != "0":
        gegevenslijst = deelnemer_gegevens.split(" ")
        aantal += 1

        print_finale_lijst(gegevenslijst, juiste_antwoorden, aantal)

        deelnemer_gegevens = input("Gegevens deelnemer: ").upper()

    """huge arrays on top, append bij elke invoer, op het einde dan een for loop met
    formatting, en huge_array[i] op de juiste plaats zetten dan"""


if __name__ == '__main__':
    main()
