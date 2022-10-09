naam = input("Naam = ")
totaal = 0
geslaagd = 0

while naam != "xx" and naam != "XX":
    totaal += 1

    test1 = int(input("Test 1: "))
    test2 = int(input("Test 2: "))
    test3 = int(input("Test 3: "))

    gemiddelde = (test1 + test2 + test3) / 3 * 100

    if gemiddelde < 70:
        resultaat = "faalt"
    else:
        resultaat = "slaagt"
        geslaagd += 1

    print(naam + " Test 1: " + str(test1) +
          " Test 2: " + str(test2) +
          " Test 3: " + str(test3) +
          " Resultaat: " + str(resultaat))

    naam = input("Naam = ")

totaal_geslaagd = geslaagd / totaal * 100

print("Er slaagden " + str(totaal_geslaagd) + "% van de " + str(totaal) + " deelnemende managers")
