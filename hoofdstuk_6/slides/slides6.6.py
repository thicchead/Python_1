def main():
    tekst = input("Tekst: ")

    middelste_letter = len(tekst) // 2

    if len(tekst) % 2 != 0:
        print(tekst[:middelste_letter] + tekst[middelste_letter].upper() + tekst[middelste_letter + 1:])

    else:
        print(tekst[:middelste_letter - 1] + tekst[middelste_letter - 1:middelste_letter + 1].upper() + tekst[middelste_letter + 1:])


if __name__ == '__main__':
    main()
