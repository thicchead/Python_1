def main():
    getallenlijst = []
    getal = int(input("Getal: "))

    while getal != 0:
        if getal in getallenlijst:
            print("Staat al op plaats " + str(getallenlijst.index(getal)))
            getallenlijst.remove(getal)
        else:
            getallenlijst.append(getal)

        getal = int(input("Getal: "))

    print(getallenlijst)


if __name__ == '__main__':
    main()
