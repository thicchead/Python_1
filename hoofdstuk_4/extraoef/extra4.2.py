naam = input("Naam student: ")

while naam != "xx" and naam != "XX":
    behaald_percentage = float(input("Behaald percentage: "))

    if behaald_percentage < 0:
        print("Fout, het getal moet minstens 0 zijn!")
        behaald_percentage = float(input("Behaald percentage: "))

    if behaald_percentage > 100:
        print("Fout, het mag niet hoger dan 100 zijn!")
        behaald_percentage = float(input("Behaald percentage: "))

    if behaald_percentage < 60:
        print("Onvoldoende")
    elif behaald_percentage < 70:
        print("Voldoende")
    elif behaald_percentage < 80:
        print("Onderscheiding")
    elif behaald_percentage < 85:
        print("Grote onderscheiding")
    else:
        print("Grootste onderscheiding")

    naam = input("Naam student: ")
