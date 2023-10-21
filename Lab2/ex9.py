def obstructed_seats(matrix):
    obstructed = []
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(0,rows):
        for j in range(0,cols):
            height = matrix[i][j]
            for k in range(i-1, 0, -1):
                if matrix[k][j] >= height:
                    obstructed.append((i, j))
                    break
    
    return obstructed
def main():
    stadium = [
        [1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5]
    ]

    result = obstructed_seats(stadium)
    print(result)

if __name__ == "__main__":
    main() 



