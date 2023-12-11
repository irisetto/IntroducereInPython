import random


class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.generator = random.Random()
        self.generate_matrix()

    def generate_matrix(self):
        self.matrix = [[self.generator.randint(1, 10) for _ in range(0, self.m)]
                       for _ in range(0, self.n)]

    def show(self, matrix=None):
        for linie in self.matrix:
            for x in linie:
                print(x, end=' ')
            print()

    def transpose(self):
        transpose_matrix = [
                        [self.matrix[j][i] for j in range(0, self.m)]
                        for i in range(0, self.n)]
        return transpose_matrix

    def multiply(self, a):
        nr_linii = len(a)
        nr_coloane = len(a[0])
        results = list()
        if self.m == nr_linii:
            for i in range(0, self.n):
                l = list()
                for j in range(0, nr_coloane):
                    result = sum(
                        self.matrix[i][k] * a[k][j] for k in range(0, nr_linii)
                    )
                    l.append(result)
                results.append(l)
        return results


    def transformation(self):
        new_map = [list(map(lambda x:x + 10, y)) for y in self.matrix]
        print(new_map)


if __name__ == '__main__':
    m = Matrix(2, 2)
    n = Matrix(2, 1)
    m.show()
    m.transformation()
    # n.show()
    # print(m.transpose())
    #
    # print(m.multiply(n.matrix))
