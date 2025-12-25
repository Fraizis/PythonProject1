def max_treasure_value() -> None:


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

        for num_1 in range(len(tunnels) - 1):
            for num_2 in range(num_1 + 1, len(tunnels)):
                    print(tunnels[num_1], tunnels[num_2])

                # if tunnels[num_1][0] not in visited_isles:
                #
                #     print(tunnels[num_1], tunnels[num_2])
                #
                #     first_isl = tunnels[num_1][0]
                #     second_isl = tunnels[num_1][1]
                #
                #     total_value += treasures[num_2]
                #
                #     visited_isles.append(first_isl)
                #
                #     if second_isl not in tunnels[num + 1]:
                #         break

    print(total_value or 0)


if __name__ == '__main__':
    max_treasure_value()
