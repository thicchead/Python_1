def bereken_schrikkeljaar(jaar):
    # if jaar % 4 == 0 and (jaar % 100 != 0 or jaar % 400 == 0):
    #     schrikkeljaar = True
    # else:
    #     schrikkeljaar = False
    #
    # return schrikkeljaar
    return jaar % 4 == 0 and (jaar % 100 != 0 or jaar % 400 == 0)


def main():
    jaar = int(input("Jaar: "))

    while jaar != 0:
        print(bereken_schrikkeljaar(jaar))

        jaar = int(input("Jaar: "))


if __name__ == '__main__':
    main()

# jaar = int(input("Jaar: "))
#
# while jaar != 0:
#     if jaar % 4 == 0 and (jaar % 100 != 0 or jaar % 400 == 0):
#         schrikkeljaar = True
#     else:
#         schrikkeljaar = False
#
#     print(schrikkeljaar)
#
#     jaar = int(input("Jaar: "))
