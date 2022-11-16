from random import randint


def main():
    aantal_gratis_dagen = randint(4, 10) * 5
    print(aantal_gratis_dagen)

    aantal_weken = aantal_gratis_dagen // 7
    aantal_gratis_dagen = aantal_gratis_dagen % 7

    print(aantal_gratis_dagen)
    print(aantal_weken)


if __name__ == '__main__':
    main()
