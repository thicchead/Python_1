def controleer(lidnummer):
    lidnummer -= lidnummer // 1000000 * 1000000
    tweede_cijfer = lidnummer // 100000
    # print(tweede_cijfer)

    lidnummer -= lidnummer // 10000 * 10000
    # print(lidnummer)
    vierde_cijfer = lidnummer // 1000
    # print(vierde_cijfer)

    gevormd_cijfer = str(tweede_cijfer) + str(vierde_cijfer)

    laatste_twee = lidnummer - lidnummer // 100 * 100
    # print(lidnummer)
    # print(laatste_twee)
    # print(gevormd_cijfer)
    # print(laatste_twee)

    if str(gevormd_cijfer) == str(laatste_twee):
        return True
    else:
        return False


def main():
    lidnummer = int(input("Lidnummer: "))

    if controleer(lidnummer):
        print("Gefeliciteerd, je moet niet betalen")
    else:
        print("Helaas, je moet betalen")


if __name__ == '__main__':
    main()
