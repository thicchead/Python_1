def main():
    tekst = input("Tekst: ")

    middelste_letter = len(tekst) // 2

    if len(tekst) % 2 != 0:
        midden = tekst[int(middelste_letter)]
        print(tekst[:middelste_letter] + midden.upper() + tekst[middelste_letter + 1:])
    else:
        midden = tekst[int(middelste_letter - 1)] + tekst[middelste_letter]
        print(tekst[:middelste_letter - 1] + midden.upper() + tekst[middelste_letter + 1:])


if __name__ == '__main__':
    main()
