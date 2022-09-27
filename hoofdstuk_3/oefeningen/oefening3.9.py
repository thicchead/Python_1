bewerkingscode = int(input("Bewerkingscode = "))

a = int(input("Getal a = "))
b = int(input("Getal b = "))

if bewerkingscode == 1:
    print(a + b)
elif bewerkingscode == 2:
    print(a - b)
elif bewerkingscode == 3:
    print(a * b)
elif bewerkingscode == 4:
    print(a ** 2)
elif bewerkingscode == 5:
    print(b ** 2)
else:
    print("Foutieve code")
