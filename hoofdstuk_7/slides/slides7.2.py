def main():
    getallenlijst = [9, 12, 7, 3, -4, 15, 7, 6, -13, 5]

    # grootste_getal = -100000
    # for getal in getallenlijst:
    #     if getal > grootste_getal:
    #         grootste_getal = getal
    # print(grootste_getal)
    #
    # kleinste_getal = 100000
    # # for getal in getallenlijst:
    # #     if getal < kleinste_getal:
    # #         kleinste_getal = getal
    # # print(kleinste_getal)
    # for i in range(len(getallenlijst)):
    #     if getallenlijst[i] < kleinste_getal:
    #         kleinste_getal = getallenlijst[i]
    # print(kleinste_getal)
    #
    # som = 0
    # for getal in getallenlijst:
    #     som += getal
    # print(som)
    """Kan ook de eerste waarde erin zetten, en dan for loop met range vanaf 1, 
    waarde 0 is al opgeslagen als eerste stap"""
    grootste = -100000
    kleinste = 100000
    som = 0
    for getal in getallenlijst:
        if getal < kleinste:
            kleinste = getal
        elif getal > grootste:
            grootste = getal
        som += getal

    print(grootste)
    print(kleinste)
    print(som)


if __name__ == '__main__':
    main()
