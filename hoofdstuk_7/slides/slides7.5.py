def vind_element(mijn_lijst, element):
    aantal_keer = 0
    indexen = []

    for i in range(len(mijn_lijst)):
        if mijn_lijst[i] == element:
            aantal_keer += 1
            indexen.append(i)

    # print("Het gevraagde element komt " + str(mijn_lijst.count(element)) + " keer voor")
    print("Het gevraagde element komt " + str(aantal_keer) + " keer voor")
    print(str(element) + " komt voor op plaatsen: " + str(indexen))


def main():
    lijst = [5, 9, 7, 6, 1, 7, 8, 3, 1, 7, 8, 5, 2, 0, 7]
    getal = 7

    vind_element(lijst, getal)


if __name__ == '__main__':
    main()
