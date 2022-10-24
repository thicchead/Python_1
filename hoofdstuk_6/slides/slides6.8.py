def main():
    spreuk = "abracadabra"

    spreuk = spreuk.replace("a", "o")
    print(spreuk)

    print(spreuk.count("o"))

    aantal = 0
    for letter in spreuk:
        if letter == "o":
            aantal += 1
    print(aantal)


if __name__ == '__main__':
    main()
