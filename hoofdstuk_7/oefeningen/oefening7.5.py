def main():
    AANTAL_KANDIDATEN = 4
    code = int(input("Code: "))

    kandidatenlijst = [0] * AANTAL_KANDIDATEN
    aantal = 0

    while code != 0:
        if code == 1:
            kandidatenlijst[0] += 1
        elif code == 2:
            kandidatenlijst[1] += 1
        elif code == 3:
            kandidatenlijst[2] += 1
        else:
            kandidatenlijst[3] += 1

        aantal += 1

        code = int(input("Code: "))

    for kandidaat in kandidatenlijst:
        print(kandidaat, end=", ")
        print(round(100 / aantal * kandidaat, 1))


if __name__ == '__main__':
    main()
