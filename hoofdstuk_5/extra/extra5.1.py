# found the code, not self written

def benader_pi(aantal_termen):
    t_sum = 0
    for i in range(aantal_termen):
        term = (-1) ** i / (2 * i + 1)
        t_sum = t_sum + term

    return t_sum * 4


def main():
    getal = int(input("Getal: "))
    print(benader_pi(getal))


if __name__ == '__main__':
    main()
