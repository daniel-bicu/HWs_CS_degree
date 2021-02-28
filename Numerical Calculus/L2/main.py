import numpy as np

from cholesky import solve

if __name__ == '__main__':
    matrix = []
    b = []

    with open('matrix.txt', 'r') as f:
        line = f.readline()
        while line:
            line = [int(i) for i in line.split(' ')]
            matrix.append(line)
            line = f.readline()

    with open('b.txt', 'r') as f:
        line = f.readline()
        b = [int(i) for i in line.split(' ')]

    n = len(matrix)

    solve(n, matrix, b)