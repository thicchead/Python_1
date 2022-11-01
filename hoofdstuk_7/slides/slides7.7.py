def get_number_of_tests(my_list):
    return len(my_list)


def get_number_of_participants(my_list):
    return len(my_list[0])


def highest_heart_rate(my_list):
    highest = 0
    for test in my_list:
        if max(test) > highest:
            highest = max(test)

    return highest


def lowest_heart_rate(my_list):
    lowest = 200

    # for test in my_list:
    #     for heart_rate in test:
    #         if heart_rate < lowest:
    #             lowest = heart_rate

    for test in my_list:
        if min(test) < lowest:
            lowest = min(test)

    return lowest


def average_heart_rate(my_list):
    for test in my_list:
        print(sum(test) / get_number_of_participants(my_list))


def heart_rate_difference(my_list):
    participant_list = []
    for i in range(get_number_of_participants(my_list)):
        participant_list.append([])
        for participant in my_list:
            participant_list[-1].append(participant[i])

    for i in range(len(participant_list)):
        print("Deelnemer: " + str(i + 1))
        print(max(participant_list[i]) - min(participant_list[i]))


def main():
    heart_rates = [[72, 75, 71, 73, 72, 76],
                   [91, 90, 94, 93, 88, 91],
                   [130, 135, 139, 142, 129, 138],
                   [120, 118, 110, 105, 121, 119]]
    print(get_number_of_tests(heart_rates))
    print(get_number_of_participants(heart_rates))
    print(highest_heart_rate(heart_rates))
    print(lowest_heart_rate(heart_rates))
    average_heart_rate(heart_rates)
    heart_rate_difference(heart_rates)


if __name__ == '__main__':
    main()
