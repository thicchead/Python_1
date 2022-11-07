from random import randint


def main():
    lijst = []

    for i in range(500):
        random_getal = randint(0, 10000)
        lijst.append(random_getal)

    aantal_kleiner = 0
    grotere_lijst = []

    for element in lijst:
        if element < 5000:
            aantal_kleiner += 1

        if aantal_kleiner < 250:
            if element > 5000:
                grotere_lijst.append(element)
        else:
            if element > 8000:
                grotere_lijst.append(element)

    print(aantal_kleiner)
    print(sum(grotere_lijst))


if __name__ == '__main__':
    main()
