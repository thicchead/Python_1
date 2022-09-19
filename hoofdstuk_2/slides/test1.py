aantal_boeken = int(input("Aantal boeken = "))

print("Het verschepen van " + str(aantal_boeken) + " boeken kost "
      + str(24.95 * aantal_boeken * 0.6 + 3 + (aantal_boeken - 1) * 0.75))
