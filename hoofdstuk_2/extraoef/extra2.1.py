VAST_BEDRAG = 20  # om de 2 weken
BTW_TARIEF = 1.21

tarief_binnenlands_gesprek_be = 0.12
prijs_buitenlandse_minuten = 0.50

binnenlandse_gesprekken = int(input("Aantal binnenlandse gesprekken: "))
buitenlandse_minuten = int(input("Aantal minuten gebeld met het buitenland: "))

totaal_prijs_binnenland = binnenlandse_gesprekken * tarief_binnenlands_gesprek_be
totaal_prijs_buitenland = buitenlandse_minuten * prijs_buitenlandse_minuten

totale_prijs = (totaal_prijs_binnenland + totaal_prijs_buitenland + VAST_BEDRAG * 2) * BTW_TARIEF

print(totale_prijs)
