def main():
    voornaam = input("Voornaam: ")
    achternaam = input("Achternaam: ")

    naam = voornaam[0].upper() + ". " + achternaam[0].upper() + achternaam[1:]

    print(naam)


if __name__ == '__main__':
    main()
