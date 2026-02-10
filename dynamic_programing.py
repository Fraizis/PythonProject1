def longest_common_subsequence():
    dp_table_blue = ["b", "l", "u", "e"]
    dp_table_clues = ["c", "l", "u", "e", "s"]
    dp_table = [[0 for i in range(len(dp_table_clues))] for i in range(len(dp_table_blue))]  # (5,4)

    # for each row
    for i in range(0, len(dp_table_blue)):
        # for each column
        for j in range(0, len(dp_table_clues)):
            if dp_table_clues[j] == dp_table_blue[i]:
                dp_table[i][j] = dp_table[i - 1][j - 1] + 1
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])

    for i in dp_table:
        print(i)


def longest_common_substring():
    dp_table_blue = ["b", "l", "u", "e"]
    dp_table_clues = ["c", "l", "u", "e", "s"]
    dp_table = [[0 for i in range(len(dp_table_clues))] for i in range(len(dp_table_blue))]  # (5,4)

    # for each row
    for i in range(0, len(dp_table_blue)):
        # for each col
        for j in range(0, len(dp_table_clues)):
            if dp_table_clues[j] == dp_table_blue[i]:
                dp_table[i][j] = dp_table[i - 1][j - 1] + 1
            else:
                dp_table[i][j] = 0

    # display table
    for i in dp_table:
        print(i)


if __name__ == '__main__':
    longest_common_substring()
