def data_centers():
    """
    Решение 5 задания
    E. Датацентры
    """
    data_centers_cables_count = input().split(' ')

    data_cables = list(map(int, data_centers_cables_count))

    centers = data_cables[0]
    cables = data_cables[1]

    links = list()

    for l in range(cables):
        link = input().split(' ')
        links.append(list(map(int, link)))

    centers_num = [i for i in range(1, centers + 1)]

    result = [[min(centers_num), max(centers_num)]]

    for i in range(len(centers_num) - 1):
        result.append([centers_num[i], centers_num[i + 1]])

    need_to_add = list()
    count = 0

    for center in result:
        if center not in links:
            count += 1
            need_to_add.append(center)

    print(count)

    if len(need_to_add) > 0:
        for link in need_to_add:
            print(f'{link[0]} {link[1]}')
    else:
        print(0)


if __name__ == '__main__':
    data_centers()
