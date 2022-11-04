def bereken_gemiddelde_aanwezigheid(aanwezigheid, bezoekers):
    totaal_minuten = aanwezigheid / bezoekers

    gemiddelde_uren = totaal_minuten // 60
    gemiddelde_minuten = totaal_minuten % 60

    print("Gemiddeld waren de bezoekers " + str(gemiddelde_uren) + " uren aanwezig en " + str(gemiddelde_minuten) + " minuten")


def bereken_duur_bezoek(uur_binnenkomen, minuut_binnenkomen, uur_buitenkomen, minuut_buitenkomen):
    uur_binnenkomen *= 60
    uur_buitenkomen *= 60

    bezoek_minuten = uur_buitenkomen + minuut_buitenkomen - (uur_binnenkomen + minuut_binnenkomen)

    return bezoek_minuten


def main():
    in_uur = int(input("Uur van binnenkomen = "))
    aantal_langer_dan_een_uur = 0
    aantal_bezoekers = 0
    totale_aanwezigheid = 0

    while in_uur != 0:
        in_minuut = int(input("Minuut van binnenkomen = "))

        uit_uur = int(input("Uur van buitenkomen = "))
        uit_minuut = int(input("Minuut van buitenkomen = "))

        duur = bereken_duur_bezoek(in_uur, in_minuut, uit_uur, uit_minuut)
        if duur > 60:
            aantal_langer_dan_een_uur += 1

        aantal_bezoekers += 1
        totale_aanwezigheid += duur

        in_uur = int(input("Uur van binnenkomen = "))

    print("Er waren " + str(aantal_langer_dan_een_uur) + " bezoekers langer dan één uur aanwezig")
    bereken_gemiddelde_aanwezigheid(totale_aanwezigheid, aantal_bezoekers)


if __name__ == '__main__':
    main()
