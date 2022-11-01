def main():
    # lijst = ["hallo", "ik", "ben", "metehan"]
    # print(len(lijst))
    #
    # for element in lijst:
    #     print(element)
    #
    # i = 0
    # while i < len(lijst):
    #     print(lijst[i])
    #
    #     i += 1
    # getallenlijst = [9, 4, 7, 5, 1, 6, 3, -2, 15]
    # grootste = 0
    # kleinste = 0
    # som = 0
    #
    # for getal in getallenlijst:
    #     if getal > grootste:
    #         grootste = getal
    #     else:
    #         kleinste = getal
    #     som += getal
    #
    # print(grootste)
    # print(kleinste)
    # print(som)
    # lijst = ["hallo", "ik", "ben", "metehan"]
    # lijst[0] = "goedemorgen"
    # print(lijst)
    # lijst.append("karakoruk")
    # lijst.insert(3, "je moeder")
    # lijst.remove("ik")
    # print(lijst)
    # a = lijst.index("ben")
    # b = lijst.count("metehan")
    # print(a)
    # print(b)
    # getal = int(input("Getal: "))
    # lijst = []
    #
    # while getal != 0:
    #     if lijst.count(getal) > 0:
    #         print("Zit er al in! Index: " + str(lijst.index(getal)))
    #         lijst.remove(getal)
    #     else:
    #         lijst.append(getal)
    #
    #     getal = int(input("Getal: "))
    #
    # print(lijst)
    # lijst = []
    # kleiner = 0
    # for i in range(10):
    #     getal = float(input("Getal: "))
    #     lijst.append(getal)
    #
    # gemiddelde = sum(lijst) / len(lijst)
    #
    # for cijfer in lijst:
    #     if cijfer < gemiddelde:
    #         kleiner += 1
    #
    # print(gemiddelde)
    # print(kleiner)
    kleuren = "paars, oranje, roze"
    kleurenlijst = kleuren.split(", ")

    print(kleurenlijst)

    getallen = list(range(1, 6))
    print(getallen)


if __name__ == '__main__':
    main()
