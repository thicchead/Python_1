def main():
    min_lijst = []
    plus_lijst = []

    for i in range(10):
        getal = float(input("Getal: "))
        if getal > 0:
            plus_lijst.append(getal)
        else:
            min_lijst.append(getal)

    print(len(min_lijst))
    print(len(plus_lijst))
    print(min_lijst)
    print(plus_lijst)
    print(min(min_lijst))


if __name__ == '__main__':
    main()
