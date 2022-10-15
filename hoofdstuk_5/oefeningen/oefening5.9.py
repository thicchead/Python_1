def reis_kosten(dagen, stad):
    autoverhuur = huurauto_kosten(dagen)
    hotelkosten = hotel_kosten(dagen - 1)
    vlucht = vliegtuig_kosten(stad)

    return autoverhuur + hotelkosten + vlucht


def huurauto_kosten(dagen):
    autoprijs = 40
    huurprijs = dagen * autoprijs

    if dagen > 7:
        huurprijs -= 50
    elif dagen > 3:
        huurprijs -= 20

    return huurprijs


def vliegtuig_kosten(stad):
    while stad != "Barcelona" and stad != "Rome" and stad != "Berlijn" and stad != "Oslo":
        print("Foute stad!")
        stad = input("Stad: ")

    ticket = 0

    if stad == "Barcelona":
        ticket = 183
    elif stad == "Rome":
        ticket = 220
    elif stad == "Berlijn":
        ticket = 125
    elif stad == "Oslo":
        ticket = 450

    return ticket


def hotel_kosten(nachten):
    hotelprijs = 140.50

    for i in range(1, nachten + 1):
        if i % 3 == 0:
            nachten -= 1

    return hotelprijs * nachten


def main():
    aantal_dagen = int(input("Aantal dagen: "))
    bestemming = input("Stad: ")

    print(reis_kosten(aantal_dagen, bestemming))


if __name__ == '__main__':
    main()
