from random import randint


def genereer_tafels():
    for i in range(5):
        print("reeks " + str(i + 1))
        for j in range(5):
            eerste_getal = randint(0, 20)
            tweede_getal = randint(0, eerste_getal)
            print(str(j + 1) + ") " + str(eerste_getal) + " - " + str(tweede_getal) + str(" = "))


def main():
    genereer_tafels()


if __name__ == '__main__':
    main()
