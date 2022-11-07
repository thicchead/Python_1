def print_naam(vn, an):
    return vn[0].upper() + ". " + an.upper() + " "


def bepaal_sterrenbeeld(datum):
    sterrenbeelden = ["waterman", "vissen", "ram", "stier", "tweelingen", "kreeft", "leeuw", "maagd", "weegschaal",
                      "schorpioen", "boogschutter", "steenbok"]

    # dag = int(datum[:2])
    # maand = int(datum[3:5])
    verjaardag = datum.split("/")
    for i in range(0, len(verjaardag)):
        verjaardag[i] = int(verjaardag[i])

    sterrenbeeld = 0

    for i in range(len(sterrenbeelden)):
        if i == verjaardag[1]:
            sterrenbeeld = sterrenbeelden[i - 2]

            if verjaardag[0] > 21:
                sterrenbeeld = sterrenbeelden[i - 1]

    return sterrenbeeld


def main():
    naam = input("Naam: ")

    while naam != "/":
        voornaam = input("Voornaam: ")
        geboortedatum = input("Geboortedatum: ")

        print(print_naam(voornaam, naam) + str(bepaal_sterrenbeeld(geboortedatum)))

        naam = input("Naam: ")


if __name__ == '__main__':
    main()
