def main():
    lengte = int(input("Hoeveel tekens wil je ingeven? "))

    som = 0

    for i in range(0, lengte):
        karakter = input("Karakter: ")

        if "a" <= karakter <= "z":
            print("kleine letter")
        elif "A" <= karakter <= "Z":
            print("hoofdletter")
        elif chr(48) <= karakter <= chr(57):
            som += int(karakter)
        else:
            print(karakter, end=" ")
            print(" is onbekend")

    print(som)


if __name__ == '__main__':
    main()
