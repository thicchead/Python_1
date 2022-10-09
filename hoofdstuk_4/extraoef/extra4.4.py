geslacht = int(input("Geslacht = "))

while geslacht == 1 or geslacht == 2:
    gelopen_afstand = float(input("Gelopen afstand in 12 minuten = "))
    afstand_in_meter = gelopen_afstand * 1000

    conditie_getal = (afstand_in_meter - 504.9) / 44.73

    if geslacht == 1:
        if conditie_getal < 36:
            print("Slechte conditie!")
        else:
            print("Gefeliciteerd, goede conditie!")
    else:
        if conditie_getal < 29:
            print("Slechte conditie!")
        else:
            print("Gefeliciteerd, goede conditie!")

    geslacht = int(input("Geslacht = "))
