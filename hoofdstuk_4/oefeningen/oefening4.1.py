gewicht_appel = int(input("Gewicht 1 appel: "))

# for i in range(1, 101):
#     print(str(i) + " appel(s) = " + str(i * gewicht_appel) + " gr.")


aantal = 1

while aantal < 101:
    print(str(aantal) + " appel(s) = " + str(aantal * gewicht_appel) + " gr.")
    aantal += 1
