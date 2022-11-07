from random import randint


def main():
    lijst = []
    aantal_kleiner = 0

    for i in range(500):
        random_getal = randint(0, 10000)
        lijst.append(random_getal)
        # aantal kleiner hier al berekenen
        if random_getal < 5000:
            aantal_kleiner += 1

    grotere_lijst = []

    for element in lijst:
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
