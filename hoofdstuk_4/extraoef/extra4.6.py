# hoogte = int(input("Hoogte: "))
# breedte = int(input("Breedte: "))

hoogte = 4
breedte = 6

# for i in range(1, hoogte + 1):
#     for j in range(1, breedte + 1):
#         print("*", end=" ")
#     print()

for i in range(1, hoogte + 1):
    for j in range(1, breedte + 1):
        if i == 1 or i == hoogte or j == 1 or j == breedte:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
