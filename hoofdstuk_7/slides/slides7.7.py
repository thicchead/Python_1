def lowest_heart_rate(my_list):
    lowest = 200
    for test in my_list:
        for heart_rate in test:
            if heart_rate < lowest:
                lowest = heart_rate

    return lowest


def highest_heart_rate(my_list):
    highest = 0
    for tests in my_list:
        for heart_rate in tests:
            if heart_rate > highest:
                highest = heart_rate

    return highest


def get_number_of_tests(my_list):
    return len(my_list)


def get_number_of_participants(my_list):
    return len(my_list[0])


def main():
    heart_rates = [[72, 75, 71, 73, 72, 76],
                   [91, 91, 94, 93, 88, 91],
                   [130, 135, 139, 142, 129, 138],
                   [120, 118, 110, 105, 121, 119]]

    # print(get_number_of_participants(heart_rates))
    print(get_number_of_participants(heart_rates))
    print(get_number_of_tests(heart_rates))
    print(highest_heart_rate(heart_rates))
    print(lowest_heart_rate(heart_rates))


if __name__ == '__main__':
    main()
