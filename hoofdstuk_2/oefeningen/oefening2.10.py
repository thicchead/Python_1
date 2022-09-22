var1 = int(input("Getal 1 = "))
var2 = int(input("Getal 2 = "))

var1 += var2
var2 = var1 - var2
var1 -= var2

print("Getal 1: " + str(var1))
print("Getal 2: " + str(var2))
