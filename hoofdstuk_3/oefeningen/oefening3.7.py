res1 = float(input("Resultaat 1: "))
res2 = float(input("Resultaat 2: "))
res3 = float(input("Resultaat 3: "))

behaald_percentage = (res1 * 5 + res2 * 5 + res3 * 5) / 3
# print(behaald_percentage)

if behaald_percentage < 60:
    print("Onvoldoende")
elif behaald_percentage < 70:
    print("Voldoende")
elif behaald_percentage < 80:
    print("Onderscheiding")
elif behaald_percentage < 90:
    print("Grote onderscheiding")
else:
    print("Grootste onderscheiding")
