def main():
    getallenlijst = []
    som = 0
    for i in range(10):
        getal = int(input("Getal: "))
        getallenlijst.append(getal)
        som += getal

    # gemiddelde = som / len(getallenlijst)
    gemiddelde = sum(getallenlijst) / len(getallenlijst)

    kleiner = 0
    for cijfer in getallenlijst:
        if cijfer < gemiddelde:
            kleiner += 1

    print(gemiddelde)
    print(kleiner)


if __name__ == '__main__':
    main()
