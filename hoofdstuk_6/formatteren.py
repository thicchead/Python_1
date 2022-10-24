def main():
    # formatteren
    tekst = "Dit is {} oefening op {} formatteringen"
    print(tekst.format(1, 2))
    print(tekst.format("één", "twee"))

    tekst = "Dit zijn {1} oefeningen op {0} formattering"
    print(tekst.format(1, 2))
    print(tekst.format("één", "twee"))

    tekst = "Dit is {:5d} oefening op {:7.2f} formatteringen"
    print(tekst.format(1, 2.2399))

    tekst = "Dit is {:<5d} oefening op {:<7.2f} formatteringen"
    print(tekst.format(1, 2))

    tekst = "Dit is {:^5d} oefening op {:^7.2f} formatteringen"
    print(tekst.format(1, 2))

    tekst = "Dit zijn {1:^4d} oefeningen op {0:^7.2f} formatteringen"
    print(tekst.format(858458.26541, 4))


if __name__ == '__main__':
    main()
