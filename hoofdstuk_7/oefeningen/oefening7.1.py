def main():
    getallenlijst = []
    for i in range(15):
        getal = int(input("Getal " + str(i + 1) + ": "))
        getallenlijst.append(getal)

    gemiddelde = sum(getallenlijst) / len(getallenlijst)

    kleiner = 0
    for element in getallenlijst:
        if element < gemiddelde:
            kleiner += 1

    print(round(gemiddelde, 1))
    print(kleiner)
    print(str(round(100 / len(getallenlijst) * kleiner, 2)) + "%")


if __name__ == '__main__':
    main()
