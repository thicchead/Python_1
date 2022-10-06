inschrijvingsnummer = int(input("Inschrijvingsnummer = "))

snelste_tijd = 60 * 60 * 24
snelste_renner = 0
aantal_renners = 0
langer_dan_een_uur = 0

while inschrijvingsnummer > 0:
    aantal_renners += 1
    tijd_in_seconden = int(input("Tijd in seconden = "))

    if tijd_in_seconden < snelste_tijd:
        snelste_tijd = tijd_in_seconden
        snelste_renner = inschrijvingsnummer

    if tijd_in_seconden > 60 * 60:
        langer_dan_een_uur += 1

    inschrijvingsnummer = int(input("Inschrijvingsnummer = "))

langer_dan_een_uur_percentage = (langer_dan_een_uur / aantal_renners) * 100

print(str(snelste_renner) + " is de snelste renner")
print(str(langer_dan_een_uur_percentage) + "% van de renners hebben er langer dan een uur over gedaan")

aantal_uren = snelste_tijd // 3600
aantal_minuten = snelste_tijd % 3600 // 60
aantal_seconden = snelste_tijd % 3600 % 60

print("De snelste renner zijn tijd is " + str(aantal_uren) + "u " +
      str(aantal_minuten) + "m " +
      str(aantal_seconden) + "s")
