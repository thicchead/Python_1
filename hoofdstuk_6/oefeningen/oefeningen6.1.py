def main():
    tekst = input("Tekst: ")

    eerste_t = tekst.lower().find("t")
    print("Index eerste t of T: " + str(eerste_t))

    if eerste_t == -1:
        print("Geen t of T in de tekst aanwezig")
    else:
        if len(tekst) % 2 != 0:
            print(tekst[:eerste_t] + tekst[eerste_t:].upper())
        else:
            print(tekst[:eerste_t] + tekst[eerste_t:].lower())


if __name__ == '__main__':
    main()
