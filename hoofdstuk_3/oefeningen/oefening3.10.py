HUIDIGE_JAAR = 2022
BASISBEDRAG = 100

leeftijd = int(input("Leeftijd = "))
aansluitingsjaar = int(input("Aansluitingsjaar = "))

jaarkorting = (HUIDIGE_JAAR - aansluitingsjaar) * 2.5
BASISBEDRAG -= jaarkorting

if leeftijd < 21 or leeftijd > 60:
    BASISBEDRAG -= 14.5

if BASISBEDRAG < 62.5:
    BASISBEDRAG = 62.5

print(BASISBEDRAG)
