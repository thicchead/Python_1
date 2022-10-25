def teken_driehoek(gr, letter):
    for i in range(1, gr + 1):
        for j in range(1, i + 1):
            print(letter, end=" ")
            letter = ord(letter) + 1
            letter = chr(letter)

            if letter > "Z":
                letter = "A"
        print()


def main():
    grootte = int(input("Grootte driehoek: "))
    beginletter = input("Beginletter: ").upper()

    teken_driehoek(grootte, beginletter)


if __name__ == '__main__':
    main()
