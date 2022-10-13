def toon_tafel(getal):
    for i in range(11):
        print(str(i) + " x " + str(getal) + " = " + str(i * getal))


def main():
    getal = int(input("Getal: "))
    toon_tafel(getal)


if __name__ == '__main__':
    main()
