def main():
    tekst = "Barefoot on the grass,# listening to our favorite song"

    plaats_tag = tekst.find("#")
    # print(plaats_tag)

    print(tekst[plaats_tag + 1:].strip())


if __name__ == '__main__':
    main()
