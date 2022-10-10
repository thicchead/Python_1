def zet_om(koers, bedrag_euro):
    return koers * bedrag_euro


def main():
    waarde_euro = float(input("Waarde één euro in dollar: "))
    bedrag = float(input("Bedrag: "))

    while bedrag != 0:
        print(zet_om(waarde_euro, bedrag))

        bedrag = float(input("Bedrag: "))


if __name__ == '__main__':
    main()

# waarde_euro = float(input("Waarde één euro in dollar: "))
# bedrag = float(input("Bedrag: "))
#
# while bedrag != 0:
#     print("Waarde in dollar: " + str(waarde_euro * bedrag))
#
#     bedrag = float(input("Bedrag: "))
