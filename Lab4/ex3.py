
class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0 for j in range(m)] for i in range(n)]

    def get(self, i, j):
        return self.matrix[i][j]

    def set(self, i, j, value):
        self.matrix[i][j] = value

    def transpose(self):
        transposed = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def multiply(self, other):
        if self.m != other.n:
            raise ValueError("Matrices cannot be multiplied")
        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                value = 0
                for k in range(self.m):
                    value += self.get(i, k) * other.get(k, j)
                result.set(i, j, value)
        return result

    def apply(self, func):
        for i in range(self.n):
            for j in range(self.m):
                self.set(i, j, func(self.get(i, j)))
   
    def print(self):
        matrix_string = ""
        for row in self.matrix:
            row_string = ""
            for item in row:
                row_string += str(item) + " "
            matrix_string += row_string.strip() + "\n"
        return matrix_string.strip()


def main():
    matrix = Matrix(7, 7)
    matrix.set(0, 0, 1)
    matrix.set(0, 1, 1)
    matrix.set(0, 2, 1)
    matrix.set(0, 3, 1)
    matrix.set(0, 4, 1)
    matrix.set(0, 5, 1)
    matrix.set(0, 6, 1)
    matrix.set(1, 0, 1)
    matrix.set(1, 1, 1)
    matrix.set(1, 2, 1)
    matrix.set(1, 3, 1)
    matrix.set(1, 4, 1)
    matrix.set(1, 5, 1)
    matrix.set(1, 6, 1)
    matrix.set(2, 0, 1)
    matrix.set(2, 1, 1)
    matrix.set(2, 2, 1)
    matrix.set(2, 3, 1)
    matrix.set(2, 4, 1)
    matrix.set(2, 5, 1)
    matrix.set(2, 6, 1)
    matrix.set(3, 0, 1)
    matrix.set(3, 1, 1)
    matrix.set(3, 2, 1)
    matrix.set(3, 3, 1)
    matrix.set(3, 4, 1)
    matrix.set(3, 5, 1)
    matrix.set(3, 6, 1)
    matrix.set(4, 0, 1)
    matrix.set(4, 1, 1)
    matrix.set(4, 2, 1)
    matrix.set(4, 3, 1)
    matrix.set(4, 4, 1)
    matrix.set(4, 5, 1)
    matrix.set(4, 6, 1)
    matrix.set(5, 0, 1)
    matrix.set(5, 1, 1)
    matrix.set(5, 2, 1)
    matrix.set(5, 3, 1)
    matrix.set(5, 4, 1)
    matrix.set(5, 5, 1)
    matrix.set(5, 6, 1)
    matrix.set(6, 0, 1)
    matrix.set(6, 1, 1)
    matrix.set(6, 2, 1)
    matrix.set(6, 3, 1)
    matrix.set(6, 4, 1)
    matrix.set(6, 5, 1)
    matrix.set(6, 6, 1)
    
    print(matrix.print())

    transposed = matrix.transpose()
    print("Transposed:")
    print(transposed.print())

    product = matrix.multiply(transposed)
    print("Matrix Multiplication:")
    print(product.print())

    matrix.apply(lambda x: x * 2)
    print("Applied Transformation:")
    print(matrix.print())

if __name__ == "__main__":
    main()