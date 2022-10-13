def get_tienden(getal):
    tiende = int(getal % 1 * 10 // 1)
    # tiende = int(getal * 10) % 10
    return tiende


def main():
    getal = float(input("Getal: "))
    print("Tiende: " + str(get_tienden(getal)))


if __name__ == '__main__':
    main()
