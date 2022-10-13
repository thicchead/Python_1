def bepaal_belasting(belastbaar_bedrag):
    if belastbaar_bedrag <= 25000:
        te_betalen = belastbaar_bedrag * 0.384
    elif belastbaar_bedrag <= 55000:
        te_betalen = 25000 * 0.384 + (belastbaar_bedrag - 25000) * 0.5
    else:
        te_betalen = 25000 * 0.384 + 30000 * 0.5 + (belastbaar_bedrag - 55000) * 0.6

    return te_betalen


def main():
    bedrag = float(input("Bedrag: "))
    print(bepaal_belasting(bedrag))


if __name__ == '__main__':
    main()
