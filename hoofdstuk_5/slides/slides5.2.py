# def print_rechthoek(hoogte, breedte, teken):
#     for i in range(hoogte):
#         for j in range(breedte):
#             print(teken, end=" ")
#         print()
def print_teken(breedte, teken):
    for i in range(breedte):
        print(teken, end=" ")
    print()


def teken_rechthoek(hoogte, breedte, teken):
    for i in range(hoogte):
        print_teken(breedte, teken)


def main():
    hoogte = int(input("Hoogte: "))
    breedte = int(input("Breedte: "))
    teken = input("Teken: ")

    # print_rechthoek(hoogte, breedte, teken)
    teken_rechthoek(hoogte, breedte, teken)


if __name__ == '__main__':
    main()
