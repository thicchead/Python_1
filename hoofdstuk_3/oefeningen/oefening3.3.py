vertrekuur = int(input("Vertrekuur = "))
vertrekminuut = int(input("Vertrekminuut = "))
vlucht_duur = int(input("Duur van uw vlucht = "))

aantal_uren = vlucht_duur // 60
aantal_minuten = vlucht_duur - aantal_uren * 60

aankomstuur = vertrekuur + aantal_uren
aankomstminuut = vertrekminuut + aantal_minuten

if aankomstminuut >= 60:
    aankomstuur += 1
    aankomstminuut -= 60

if aankomstminuut < 10:
    aankomstminuut = "0" + str(aankomstminuut)

if aankomstuur >= 24:
    aankomstuur -= 24

print("U komt aan om " + str(aankomstuur) + "u" + str(aankomstminuut) + ".")
