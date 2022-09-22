bedrag = int(input("Aantal centen = "))

twee_euro = bedrag // 200
bedrag %= 200

een_euro = bedrag // 100
bedrag %= 100

vijftig_cent = bedrag // 50
bedrag %= 50

twintig_cent = bedrag // 20
bedrag %= 20

tien_cent = bedrag // 10
bedrag %= 10

vijf_cent = bedrag // 5
bedrag %= 5

twee_cent = bedrag // 2
bedrag %= 2

een_cent = bedrag // 1

print(str(twee_euro) + " x 2 euro")
print(str(een_euro) + " x 1 euro")
print(str(vijftig_cent) + " x 50 cent")
print(str(twintig_cent) + " x 20 cent")
print(str(tien_cent) + " x 10 cent")
print(str(vijf_cent) + " x 5 cent")
print(str(twee_cent) + " x 2 cent")
print(str(een_cent) + " x 1 cent")
