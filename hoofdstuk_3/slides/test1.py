"""print(9 < 10)
print(9 <= 10)
print(9 > 10)
print(9 == 9.0)
print(9 == "9")
print("Jan" == "jan")
print("Jan" == "Jan ")
print("Jan" > "Annita")
print("Jan" > "annita")
print("Jan" > "123")

print("7" < "21")

print("x" > "X")"""

"""print("e" in "Metehan")
print("x" in "Metehan")
print("Van" in "Metehan")"""

"""a = False
b = True
c = True

print((a and b) or c)
print(a and (b or c))"""

"""getal = int(input("Getal = "))

if getal % 2 == 0:
    print("Getal is even")
else:
    print("Getal is oneven")"""

"""gewicht = float(input("Gewicht = "))

if gewicht > 20:
    print("Te zwaar")
elif gewicht == 20:
    print("Precies goed")
else:
    print("Goede reis")"""

"""lengte = float(input("Lengte = "))
gewicht = float(input("Gewicht = "))

bmi = gewicht / (lengte * lengte)

print(bmi)

if bmi < 18:
    print("Ondergewicht")
elif bmi < 25:
    print("Ok")
elif bmi < 30:
    print("Overgewicht")
elif bmi < 40:
    print("Obesitas")
else:
    print("Ziekelijk overgewicht")"""

burgerlijke_staat = int(input("Burgerlijke staat (1-3): "))
leeftijd = int(input("Leeftijd: "))

lidgeld = 0

"""if burgerlijke_staat == 1:
    lidgeld = 25
elif burgerlijke_staat == 2:
    lidgeld = 20
else:
    lidgeld = 15"""

"""if burgerlijke_staat == 1 and leeftijd < 30:
    lidgeld = 25
else:
    lidgeld = 15"""

"""if leeftijd < 30 or burgerlijke_staat == 1:
    lidgeld = 25
else:
    lidgeld = 15"""

"""if burgerlijke_staat == 1:
    lidgeld = 25
elif burgerlijke_staat == 2 and leeftijd < 30:
    lidgeld = 20
else:
    lidgeld = 15"""

print(lidgeld)
