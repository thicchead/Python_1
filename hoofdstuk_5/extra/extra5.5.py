def bereken_bijslag(hoeveelste_kind, lt, code):
    basisbijslag = 75
    if hoeveelste_kind > 1:
        basisbijslag += (hoeveelste_kind - 1) * 70

    if code == "H":
        basisbijslag += 225

    if lt >= 12:
        basisbijslag += 50
    elif lt >= 6:
        basisbijslag += 25

    return basisbijslag


def main():
    aantal_kinderen = int(input("Aantal kinderen: "))
    totaal = 0

    for i in range(1, aantal_kinderen + 1):
        leeftijd = int(input("Leeftijd: "))
        code = input("Code: ").upper()

        kinderbijslag = bereken_bijslag(i, leeftijd, code)
        totaal += kinderbijslag

    print(totaal)


if __name__ == '__main__':
    main()
