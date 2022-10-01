# for i in range(5):
#     print(i)
#
# # Opdracht 4
# for i in range(1, 6, 2):
#     print(i)
#     print("De waarde van het kwadraat van " + str(i) + " is " + str(i ** 2))
# print()
# print("De waarde van i na afloop van de for-lus is " + str(i))

# # Opdracht 5
# for i in range(400, 349, -1):
#     print(i)

# # Opdracht 6
# for i in range(0, 200, 7):
#     print(i)

# # Opdracht 7
# for i in range(-10, 11):
#     if i > 0:
#         print("+" + str(i))
#     else:
#         print(i)

# # Opdracht 8
# for i in range(0, 10001, 28):
#     if i % 6 == 0:
#         print(i)

# # Opdracht 9
totaal = 0
for i in range(29):
    leeftijd = int(input("Leeftijd student " + str(i + 1) + " = "))
    totaal += leeftijd

print(totaal / 28)
