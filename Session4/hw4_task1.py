# Use functional tools to implement function, which calculates multiplication of two matrices
from functools import reduce


def matrix_mult(a, b):
    trans_b = list(map(list, zip(*b)))

    mult_two = lambda x, y: x * y
    sum_two = lambda x, y: x + y

    n = len(a)
    m = len(trans_b)
    return [[reduce(sum_two, map(mult_two, a[i], trans_b[j]), 0) for j in range(m)] for i in range(n)]

# example
a = [[1, 2, 3], [4, 5, 6]]
b = [[10, 20], [30, 40], [50, 60]]
print(matrix_mult(a, b))
