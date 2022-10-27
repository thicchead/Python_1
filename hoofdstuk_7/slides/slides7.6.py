def cumulative_sum(mijn_lijst):
    # fout: for i in range(len(mijn_lijst):

    for i in range(1, len(mijn_lijst)):
        # mijn_lijst[i] = mijn_lijst[i] + mijn_lijst[i - 1]
        mijn_lijst[i] = mijn_lijst[i - 1] + mijn_lijst[i]

    print(mijn_lijst)


def main():
    lijst = [1, 2, 3, 4]
    stringlijst = ["a", "b", "c"]

    cumulative_sum(lijst)
    cumulative_sum(stringlijst)


if __name__ == '__main__':
    main()
