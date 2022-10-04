temperatuur = float(input("Temperatuur = "))

aantal_nachten = 1
totaal = 0

laagste_temperatuur = 100

while aantal_nachten < 11:
    if temperatuur < laagste_temperatuur:
        laagste_temperatuur = temperatuur

    totaal += temperatuur
    aantal_nachten += 1

    temperatuur = float(input("Temperatuur = "))

print(totaal / aantal_nachten)
print(laagste_temperatuur)
