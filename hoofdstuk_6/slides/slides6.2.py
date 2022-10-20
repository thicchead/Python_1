def main():
    tekst = input("Tekst: ")

    # for letter in tekst:
    #     if letter in "aeiou":
    #         print(tekst[letter])

    for i in range(len(tekst)):
        if tekst[i] in "aeiou":
            print(i)


if __name__ == '__main__':
    main()
