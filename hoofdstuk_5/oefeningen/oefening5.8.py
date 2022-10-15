# def bereken_werknemers(uren):
#     uren = int(uren)
#     aantal_werknemers = 1
#
#     for i in range(1, uren + 1):
#         if i % 8 == 0:
#             aantal_werknemers += 1
#
#     print("Aantal werknemers nodig: " + str(aantal_werknemers))

def print_werknemers(oppervlakte):
    aantal_acht_uur = oppervlakte // 1280
    resterende_opp = oppervlakte % 1280
    minder_dan_acht = resterende_opp / 160

    print("Aantal werknemers die 8u moeten werken: " + str(int(aantal_acht_uur)))
    print("Plus 1 werknemer die " + str(minder_dan_acht) + " uur werkt")


def bereken_kostprijs(oppervlakte):
    aantal_uren = oppervlakte / 160
    uit_te_betalen = aantal_uren * 12.5

    # bereken_werknemers(aantal_uren)

    print("Te betalen lonen: " + str(uit_te_betalen))


def main():
    schoon_te_maken_oppervlakte = float(input("Schoon te maken oppervlakte: "))

    while schoon_te_maken_oppervlakte != 0:
        bereken_kostprijs(schoon_te_maken_oppervlakte)
        print_werknemers(schoon_te_maken_oppervlakte)

        schoon_te_maken_oppervlakte = float(input("Schoon te maken oppervlakte: "))


if __name__ == '__main__':
    main()
