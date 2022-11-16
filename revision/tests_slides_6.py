# tekst = input("Tekst: ")
# for i in range(len(tekst)):
#     if tekst[i] in "aeiou":
#         print(str(tekst[i]) + " op plaats: " + str(i))
#


# tekst_een = input("Tekst 1: ")
# tekst_twee = input("Tekst 2: ")
#
# kortste_tekst = tekst_een
# andere_tekst = tekst_twee
#
# if len(tekst_twee) < len(tekst_een):
#     kortste_tekst = tekst_twee
#     andere_tekst = tekst_een
#
# for i in range(len(kortste_tekst)):
#     if kortste_tekst[i] == andere_tekst[i]:
#         print("Letter " + str(kortste_tekst[i]) + " op index " + str(i))

# naam = "metjehan"
#
# naam = naam[:3] + naam[4:]
# print(naam)

# print("    what the heeeeeeeeeeeeeeeeeeeeeellllll    ".strip())
# url = "www.blabla.be"
# print(url.strip("w.be"))

# spreuk = " aBRAcaDAbra "
# spreuk = spreuk.strip()
#
# print(spreuk.upper())
# print(spreuk.lower())

# woord = input("Geef me een woord: ")
# while woord != "":
#     middelste_letter = int(len(woord) / 2 - 1)
#
#     if len(woord) % 2 == 0:
#         midden = woord[middelste_letter:middelste_letter + 2]
#         print(woord[:middelste_letter] + midden.upper() + woord[middelste_letter + 2:])
#     else:
#         print(woord[:middelste_letter + 1] + woord[middelste_letter + 1].upper() + woord[middelste_letter + 2:])
#
#     woord = input("Geef me een woord: ")


"""ord geeft een getal terug
   chr geeft een letter terug"""


def text_cleaner(text):
    for i in text:
        if i > 'z' or i < 'a':
            text = text.replace(i, " ")  # STRINGS ARE IMMUTABLE BITCH

    return text


def main():
    unclean_text = input("Text: ")
    clean_text = text_cleaner(unclean_text)
    print(clean_text)


if __name__ == '__main__':
    main()
