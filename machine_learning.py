def matrix() -> None:
    rows = 3
    columns = 3
    empty_matrix = [[0 for _ in range(columns)] for i in range(rows)]
    print(empty_matrix)

    original_matrix = [[1, 2, 3], [4, 5, 6]]
    transposed_matrix = [[row[i] for row in original_matrix] for i in range(len(original_matrix[0]))]
    print(transposed_matrix)
