from random import randint


def geef_feedback(random_getal, gok):
    if gok < random_getal:
        print("Hoger")
    elif gok == random_getal:
        print("Proficiat, getal geraden")
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
            aantal_gokken += 3

if __name__ == '__main__':
    main()
