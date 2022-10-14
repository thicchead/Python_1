from random import randint


def geef_feedback(getal, gok):
    if gok < getal:
        print("Hoger")
    elif gok == getal:
        print("Proficiat, getal geraden!")
    else:
        print("Lager")


def main():
    random_getal = randint(1, 10)
    print(random_getal)

    aantal_gokken = 0
    while aantal_gokken < 4:
        gebruiker_gok = int(input("Uw gok: "))
        geef_feedback(random_getal, gebruiker_gok)

        if gebruiker_gok != random_getal:
            aantal_gokken += 1
        else:
            aantal_gokken += 10

        if aantal_gokken == 4 and gebruiker_gok != random_getal:  # Zelf erbij gezet zodat het spel niet abrupt stopt na de 3e keer fout raden
            print("Teveel gegokt!")


if __name__ == '__main__':
    main()
