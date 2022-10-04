getal = int(input("Getal = "))

totaal = 0
totaal_negatief = 0

while getal != 0:
    totaal += getal

    if getal < 0:
        totaal_negatief += 1

    getal = int(input("Getal = "))

print(totaal)
print(totaal_negatief)
