def vervang(tekst):
    for letter in tekst:
        if letter < "a" or letter > "z":
            tekst = tekst.replace(letter, " ")

    print(tekst)


def main():
    originele_tekst = "ph@t l00t"

    vervang(originele_tekst)


if __name__ == '__main__':
    main()
