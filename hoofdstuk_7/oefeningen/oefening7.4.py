def main():
    tekst = input("Tekst: ").lower()

    letterlijst = []
    for letter in tekst:
        letterlijst.append(letter)

    for element in letterlijst:
        print(element, end=" ")
        print(letterlijst.count(element))


if __name__ == '__main__':
    main()
