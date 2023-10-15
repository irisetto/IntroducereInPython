def spiral_order(matrix):
    result = []
    rows = len(matrix)
    cols = len(matrix[0])

    top_row = 0
    bottom_row = rows - 1
    left_col = 0
    right_col = cols - 1

    while top_row <= bottom_row and left_col <= right_col:
        for i in range(left_col, right_col + 1):
            result.append(matrix[top_row][i])

        top_row += 1

        for i in range(top_row, bottom_row + 1):
            result.append(matrix[i][right_col])

        right_col -= 1

        if top_row <= bottom_row:
            for i in range(right_col, left_col - 1, -1):
                result.append(matrix[bottom_row][i])

            bottom_row -= 1

        if left_col <= right_col:
            for i in range(bottom_row, top_row - 1, -1):
                result.append(matrix[i][left_col])

            left_col += 1

    return ''.join(result)

matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]
print(spiral_order(matrix))
