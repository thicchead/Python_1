# grootte = int(input("Grootte driehoek = "))
grootte = 5

for i in range(grootte, 0, -1):
    for j in range(i):
        print("@", end=" ")
    print()
