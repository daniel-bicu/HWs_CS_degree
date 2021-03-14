import copy
from math import fabs


def add(rare_matrix, triag_matrix):
    rare_matrix_clone = copy.deepcopy(rare_matrix)
    dim_matrix = len(list(rare_matrix_clone))
    (t, a), (p, b), (q, c) = triag_matrix

    for i in range(dim_matrix):
        if i in rare_matrix_clone[i]:
            rare_matrix_clone[i][i] = rare_matrix_clone[i][i] + a[f'{i}:{i}']
        else:
            rare_matrix_clone[i][i] = a[f'{i}:{i}']

    for k in range(dim_matrix - p):
        i = k
        j = k + p

        if j in rare_matrix_clone[i]:
            rare_matrix_clone[i][j] = rare_matrix_clone[i][j] + b[f'{i}:{j}']
        else:
            rare_matrix_clone[i][j] = b[f'{i}:{j}']

    for k in range(dim_matrix - q):
        i = k + q
        j = k

        if j in rare_matrix_clone[i]:
            rare_matrix_clone[i][j] = rare_matrix_clone[i][j] + c[f'{i}:{j}']
        else:
            rare_matrix_clone[i][j] = c[f'{i}:{j}']

    return rare_matrix_clone


def filter_tridiag(tridiag, j):
    some = filter(lambda e: int(e[0].split(':')[0]) == j, tridiag.items())
    some = dict(some)

    if len(some.keys()):
        key = list(some.keys())[0]
        some = list(some.keys())[0]
        some = [int(i) for i in some.split(':')]
        some.append(tridiag[key])
    else:
        some = None

    return some


def update_cell(matrix_clone, tridiag_matrix, i, j, value):
    k_elem = filter_tridiag(tridiag_matrix, j)
    if k_elem is not None:
        k_i, k_j, k_value = k_elem
        if k_j in matrix_clone[i]:
            matrix_clone[i][k_j] = matrix_clone[i][k_j] + (value * k_value)
        else:
            matrix_clone[i][k_j] = value * k_value


def multiply(rare_matrix, triag_matrix):
    dim_matrix = len(list(rare_matrix))
    (t, a), (p, b), (q, c) = triag_matrix

    rare_matrix_clone = {}
    for i in range(dim_matrix):
        rare_matrix_clone[i] = {}

    for i in range(dim_matrix):
        if len(rare_matrix[i].keys()) == 0:
            continue
        for j, value in rare_matrix[i].items():
            update_cell(rare_matrix_clone, a, i, j, value)
            update_cell(rare_matrix_clone, b, i, j, value)
            update_cell(rare_matrix_clone, c, i, j, value)

        # print(i, rare_matrix_clone[i])

    return rare_matrix_clone


def multiply_triag(triag_matrix_a, triag_matrix_b):
    (A_t, A_a), (A_p, A_b), (A_q, A_c) = triag_matrix_a
    (B_t, B_a), (B_p, B_b), (B_q, B_c) = triag_matrix_b

    n = len(list(A_a))
    rare_matrix_clone = {}
    for i in range(n):
        rare_matrix_clone[i] = {}

    for key, value in A_a.items():
        i, j = [int(k) for k in key.split(':')]
        update_cell(rare_matrix_clone, B_a, i, j, value)
        update_cell(rare_matrix_clone, B_b, i, j, value)
        update_cell(rare_matrix_clone, B_c, i, j, value)

    for key, value in A_b.items():
        i, j = [int(k) for k in key.split(':')]
        update_cell(rare_matrix_clone, B_a, i, j, value)
        update_cell(rare_matrix_clone, B_b, i, j, value)
        update_cell(rare_matrix_clone, B_c, i, j, value)

    for key, value in A_c.items():
        i, j = [int(k) for k in key.split(':')]
        update_cell(rare_matrix_clone, B_a, i, j, value)
        update_cell(rare_matrix_clone, B_b, i, j, value)
        update_cell(rare_matrix_clone, B_c, i, j, value)

    return rare_matrix_clone


def display_matrix(rare_matrix):
    n = len(rare_matrix.keys())

    for i in range(n):
        keys = sorted(rare_matrix[i])
        line = ''
        for j in keys:
            line += f'{j}:{rare_matrix[i][j]} '
        print(i, line)


def check(rare_matrix_a, rare_matrix_b, epsilon = 10 ** (-6)):
    dim_matrix = len(rare_matrix_a.keys())
    n = 0
    nr = 0

    for i in range(dim_matrix):
        for j, value in rare_matrix_a[i].items():
            n += 1
            if fabs(value - rare_matrix_b[i][j]) >= epsilon:
                nr += 1

    return nr / n