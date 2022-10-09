PRIJS_JETON = 0.70


for i in range(1, 51):
    print(str(i) + " jetons = " + str(i * PRIJS_JETON))

    if i > 24:
        if i % 5 == 0:
            i += 5
