def cumulative_sum(gegeven_lijst):
    for i in range(1, len(gegeven_lijst)):
        gegeven_lijst[i] = gegeven_lijst[i - 1] + gegeven_lijst[i]

    print(gegeven_lijst)


def main():
    lijst = [1, 2, 3, 4, 5]
    cumulative_sum(lijst)

    stringlijst = ["a", "b", "c", "d", "e"]
    cumulative_sum(stringlijst)


if __name__ == '__main__':
    main()
