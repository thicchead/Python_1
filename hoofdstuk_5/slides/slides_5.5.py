def is_even(getal):
    if getal % 2 == 0:
        return True
    else:
        return False


def is_oneven(getal):
    return not(is_even(getal))


def main():
    print(is_oneven(10))
    print(is_even(10))

    print(is_oneven(11))
    print(is_even(11))


if __name__ == '__main__':
    main()
