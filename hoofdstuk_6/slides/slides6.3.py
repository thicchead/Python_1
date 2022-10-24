def main():
    s1 = input("Eerste string: ")
    s2 = input("Tweede string: ")

    kleinste_string = len(s1)

    if len(s2) < kleinste_string:
        kleinste_string = len(s2)

    for i in range(kleinste_string):
        if s1[i] == s2[i]:
            print(s1[i], end=" ")
            print(i)


if __name__ == '__main__':
    main()
