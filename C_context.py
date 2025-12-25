def context():

    string_count = int(input())

    strings_list = list()
    for num in range(string_count):
        string_length = int(input())
        string = input().split(' ')
        strings_list.append(string)

    print(strings_list)

    # strings_list = [
    #     ['small', 'prompt'],
    #     ['a', 'four', 'word', 'prompt'],
    #     ['unique', 'line', 'with', 'y', 'words'],
    #     ['a', 'lines', 'r', 'i', 'w']
    # ]

    count = 0
    cont_dict = dict()
    cont_list = list()
    cont_set = set()
    string_count = len(strings_list)
    max_length = 0

    strings_list.sort(key=len)

    string_list_copy = strings_list[:]

    print(strings_list)

    print(string_list_copy)

    if string_count > 1:
        for lst in range(len(strings_list)):
            if lst + 1 < len(strings_list):
                for lst_2 in range(lst + 1, len(strings_list)):

                    first_string = strings_list[lst]
                    second_string = strings_list[lst_2]

                    for sym in first_string:
                        if sym in second_string:
                            count += 1
                            first = set([i for i in first_string])
                            second = set([i for i in second_string])
                            first_string.extend(second_string)

                            first.update(second)
                            # print(second_string)

                            string_list_copy.append(first)

                            cont_list.append(first)
                            max_length += 1
                            break

                    if count == len(strings_list) - 1:
                        break

        print(f'{string_count - max_length}')

    else:
        print(f'{string_count} {len(strings_list[0])}')


if __name__ == '__main__':
    context()
