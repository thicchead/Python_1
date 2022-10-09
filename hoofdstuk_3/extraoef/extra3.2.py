leeftijd = int(input("Leeftijd = "))

if leeftijd < 12:
    lidgeld = 6
elif leeftijd < 18:
    lidgeld = 12.5
else:
    lidgeld = 25

print(leeftijd)
print(lidgeld)
