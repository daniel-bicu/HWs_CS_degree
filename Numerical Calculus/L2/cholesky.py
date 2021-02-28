import math
import numpy as np
from scipy.linalg import lu, inv



def l_pp(matrix, p):
    sum = 0

    for j in range(0, p):
        sum += matrix[p][j] ** 2

    return math.sqrt(matrix[p][p] - sum)


def l_ip(matrix, i, p):
    sum = 0

    for j in range(0, p):
        sum += (matrix[i][j] * matrix[p][j])

    return (matrix[i][p] - sum) / matrix[p][p]


def build_matrix(n, matrix, diag):
    for j in range(0, n):
        for i in range(0, n):
            if i < j:
                matrix[i][j] = 0
            elif i == j:
                diag.append(l_pp(matrix, i))
                matrix[i][j] = diag[i]
            else:
                matrix[i][j] = l_ip(matrix, i, j)


def solve_equation_lower_triangular(n, matrix, b):
    y = [0 for i in range(0, n)]

    for i in range(0, n):
        sum = 0
        for j in range(0, i):
            sum += (matrix[i][j] * y[j])
        y[i] = (b[i] - sum) / matrix[i][i]

    return y


def solve_equation_upper_triangular(n, matrix, b):
    y = [0 for i in range(0, n)]

    for i in range(n - 1, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += (matrix[i][j] * y[j])
        y[i] = (b[i] - sum) / matrix[i][i]

    return y


def solve_llt(n, matrix, b):
    y = solve_equation_lower_triangular(n, matrix, b)
    x = solve_equation_upper_triangular(n, np.array(matrix).T, y)

    return x


def solve_lu(n, L, U, b, p):
    b = p.dot(b)

    y = solve_equation_lower_triangular(n, L, b)
    x = solve_equation_upper_triangular(n, U, y)

    return x


def det(diag):
    prod = 1
    for val in diag:
        prod *= (val ** 2)

    return prod


def aprox_error(matrix, x_chol, b):
    matrix = np.array(matrix)
    A = matrix.dot(matrix.T)
    A = A.dot(x_chol)
    A = A - b
    return np.linalg.norm(A)


def aprox_reverse(n, matrix):
    diag = []
    build_matrix(3, matrix, diag)
    e = [0 for i in range(n)]
    A_reverse = [[0 for i in range(n)] for i in range(n)]

    for j in range(n):
        e[j] = 1
        x = solve_llt(n, matrix, e)
        for i in range(n):
            A_reverse[i][j] = x[i]
        e[j] = 0

    return A_reverse


def frobenius_norm(matrix_a, matrix_b):
    matrix_b = inv(matrix_b)
    print('Inversa A python\n', matrix_b)
    dif = matrix_a - matrix_b
    return np.linalg.norm(dif, 'fro')


def solve(n, matrix, b):
    diag = []
    matrix = np.array(matrix)
    matrix = matrix.astype(np.float)
    print('Matricea initiala\n', matrix)
    print('\n')

    build_matrix(n, matrix, diag)
    print('Decompunerea L Cholesky\n', matrix)
    print('\n')

    print('Determinantul', det(diag))
    print('\n')

    X = solve_llt(n, matrix, b)
    A = matrix.dot(matrix.T)
    print('Calculare Ax=b')
    print('A\n', A)
    print('b', b)
    print('Solutia X Cholesky', X)
    print('\n')

    print('Aproximarea erorii solutiei\n', aprox_error(matrix, X, b))
    print('\n')

    p, L, U = lu(A)
    X = solve_lu(n, L, U, b, p)
    print('LU Decomposition')
    print('p\n', p)
    print('L\n', L)
    print('U\n', U)
    print('Solutia X LU', X)
    print('\n')

    MATRIX = A
    MATRIX = MATRIX.astype(np.float)
    A_i_Cholesky = aprox_reverse(n, MATRIX)
    print('Inversa matricei')
    print('Matricea\n', A)
    print('Inversa\n', np.array(A_i_Cholesky))
    print('Verificarea corectitudii', A.dot(A_i_Cholesky))
    print('\n')

    print('Norma Frobenius')
    print(frobenius_norm(A_i_Cholesky, A))


if __name__ == '__main__':
    matrix = [
        [1, 0, 3],
        [0, 4, 2],
        [3, 2, 11]
    ]
    b = [1, 2, 4]
    solve(3, matrix, b)