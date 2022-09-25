getal1 = int(input("Getal 1 = "))
getal2 = int(input("Getal 2 = "))

if getal1 < getal2:
    kleinste_getal = getal1
    grootste_getal = getal2
else:
    kleinste_getal = getal2
    grootste_getal = getal1

print(kleinste_getal ** 2)

if kleinste_getal == 0:
    print("Je kan niet delen door 0")
else:
    print(grootste_getal / kleinste_getal)
