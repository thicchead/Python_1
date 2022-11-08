def main():
    totalelijst = []
    for i in range(1, 6):
        punten = (input("Punten: "))
        puntenlijst = punten.split(" ")

        totalelijst.append(puntenlijst)

    vakkenlijst = []
    for i in range(len(totalelijst[0])):
        vakkenlijst.append([])
        for punt in totalelijst:
            vakkenlijst[-1].append(int(punt[i]))  # strings hier naar int veranderd

    for row in vakkenlijst:
        print("Minimum: " + str(min(row)))
        print("Gemiddelde: " + str(round(sum(row) / 5, 1)))
        for element in row:
            if element == min(row):
                print("Student met het laagste punt: " + str(row.index(element) + 1))


if __name__ == '__main__':
    main()
