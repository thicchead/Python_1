def print_element(getallenlijst, element):
    print(getallenlijst.count(element))
    indices = []

    for i in range(len(getallenlijst)):
        if getallenlijst[i] == element:
            indices.append(i)

    print(indices)


def main():
    lijst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 4, 1, 9, 3, 7, 6]
    cijfer = 4

    print_element(lijst, cijfer)


if __name__ == '__main__':
    main()
