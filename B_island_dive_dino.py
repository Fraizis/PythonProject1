

def time_island_dive():
    first_input = input().split(' ')

    cords_list = list()

    for num in range(int(first_input[0])):
        string = input()
        cords_list.append(string)

    for t in cords_list:
        print(t)


if __name__ == '__main__':
    time_island_dive()
