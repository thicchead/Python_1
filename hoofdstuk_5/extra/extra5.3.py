from random import randint


def genereer_getal():
    viercijferig_getal = ""

    for i in range(4):
        random_getal = randint(1, 3)
        random_getal = str(random_getal)
        viercijferig_getal += random_getal

    return int(viercijferig_getal)


def perfectgetal(get):
    totaal = 0
    for i in range(1, get):
        if get % i == 0:
            totaal += i

    if totaal == get:
        print("Perfect")
    else:
        print("Niet perfect")


def main():
    for i in range(10):
        getal = randint(1, 100)

        print("Random getal: " + str(getal), end=", ")
        perfectgetal(getal)
        print("Getal met 4 cijfers, allemaal onder de 3: " + str(genereer_getal()), end=", ")
        perfectgetal(genereer_getal())


if __name__ == '__main__':
    main()
