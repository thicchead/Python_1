def main():
    eerste_tekst = input("Tekst 1: ") + "****"
    tweede_tekst = "++++" + input("Tekst 2: ")
    # print(eerste_tekst)
    # print(tweede_tekst)

    print(eerste_tekst[:4].upper() + tweede_tekst[-4:].lower())


if __name__ == '__main__':
    main()
