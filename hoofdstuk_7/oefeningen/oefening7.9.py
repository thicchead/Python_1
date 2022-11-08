def main():
    t_shirts = [[45, 102, 19, 55, 0],
                [79, 47, 58, 22, 46],
                [109, 33, 112, 0, 0]]

    te_weinig = []

    for i in range(len(t_shirts)):
        maattotaal = sum(t_shirts[i]) / 3

        for j in range(0, len(t_shirts[0])):
            if t_shirts[i][j] < maattotaal:
                if i == 0:
                    te_weinig.append("small")
                    if j == 0:
                        te_weinig.append("rood")
                    elif j == 1:
                        te_weinig.append("wit")
                    elif j == 2:
                        te_weinig.append("blauw")
                    elif j == 3:
                        te_weinig.append("oranje")
                    else:
                        te_weinig.append("zwart")

    print(te_weinig)


if __name__ == '__main__':
    main()
