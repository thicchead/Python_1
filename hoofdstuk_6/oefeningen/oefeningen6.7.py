from random import randint


def encrypteer(normale_tekst, random_getal):
    nieuwe_tekst = ""
    for letter in normale_tekst:
        letter = ord(letter) + random_getal
        nieuwe_tekst += chr(letter)

    return nieuwe_tekst


def main():
    tekst = input("Tekst: ")
    # getal = 4
    getal = randint(1, 12) * 2
    print(getal)
    print(encrypteer(tekst, getal))


if __name__ == '__main__':
    main()
