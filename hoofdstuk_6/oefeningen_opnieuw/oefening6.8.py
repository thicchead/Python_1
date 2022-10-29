def maak_driehoek(letter, basis):
    for i in range(1, basis + 1):
        for j in range(i):
            print(letter, end=" ")
            letter = ord(letter) + 1
            letter = chr(letter)

            if letter > "Z":
                letter = "A"
        print()


def main():
    beginletter = input("Beginletter: ").upper()
    grootte = int(input("Grootte driehoek: "))

    maak_driehoek(beginletter, grootte)

    # for i in range(1, 5):
    #     for j in range(i):
    #         print("*", end="")
    #     print()


if __name__ == '__main__':
    main()
