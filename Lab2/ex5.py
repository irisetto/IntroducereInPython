def replace_below_main_diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i > j:
                matrix[i][j] = 0
    return matrix

def main():
    matrix = [
        [1, 2, 3, 5],
        [4, 5, 6, 5],
        [7, 8, 9, 5],
        [7, 8, 9, 5]
    ]
    result_matrix = replace_below_main_diagonal(matrix)
    for row in result_matrix:
        print(row)

if __name__ == "__main__":
    main()