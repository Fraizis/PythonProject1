def max_treasure_value() -> None:
    """
    Решение 1 задания
    A. Сокровища островов пирата Дино
    """
    islands_tunnels_count = input().split(' ')

    island_tunnels = list(map(int, islands_tunnels_count))

    islands = island_tunnels[0]

    tunnels_count = island_tunnels[1]

    treasure_values = input().split(' ')

    if len(treasure_values) != islands or islands == 0:
        print(0)
        return

    treasures = list(map(int, treasure_values))

    tunnels = list()

    for tun in range(tunnels_count):
        tunnel = input().split(' ')
        tunnels.append(list(map(int, tunnel)))

    visited_isles = list()
    total_value = treasures[0]

    if tunnels_count != 0:

        for num in range(len(tunnels)):
            if num + 1 < len(tunnels):
                if tunnels[num][0] not in visited_isles:
                    first_isl = tunnels[num][0]
                    second_isl = tunnels[num][1]

                    total_value += treasures[num + 1]

                    visited_isles.append(first_isl)

                    if second_isl not in tunnels[num + 1]:
                        break

    print(total_value or 0)


if __name__ == '__main__':
    max_treasure_value()
