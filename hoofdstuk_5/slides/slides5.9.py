from random import randint


def main():
    print("Opdracht 1: " + str(randint(0, 10)))

    for i in range(10):
        print("Opdracht 2: " + str(randint(1, 9)))

    print("Opdracht 3: " + str(randint(-20, 100) * 10))

    print("Opdracht 4: " + str(randint(0, 999) / 10))


if __name__ == '__main__':
    main()
