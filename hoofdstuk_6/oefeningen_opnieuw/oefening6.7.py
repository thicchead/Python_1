from random import randint


def encrypteer_tekst(tekst, getal):
    for letter in tekst:
        letter = ord(letter) + getal
        letter = chr(letter)
        print(letter, end="")


def main():
    tekst = input("Tekst: ")
    random_getal = randint(1, 12) * 2

    encrypteer_tekst(tekst, random_getal)


if __name__ == '__main__':
    main()
