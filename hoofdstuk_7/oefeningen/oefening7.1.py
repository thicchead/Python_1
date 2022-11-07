def main():
    getallenlijst = []
    for i in range(15):
        getal = int(input("Getal " + str(i + 1) + ": "))
        getallenlijst.append(getal)

    gemiddelde = sum(getallenlijst) / len(getallenlijst)

    kleiner_dan_gemiddelde = 0
    for element in getallenlijst:
        if element < gemiddelde:
            kleiner_dan_gemiddelde += 1

    print(round(gemiddelde, 1))
    print(kleiner_dan_gemiddelde)
    print(str(round(100 / len(getallenlijst) * kleiner_dan_gemiddelde, 2)) + "%")


if __name__ == '__main__':
    main()
