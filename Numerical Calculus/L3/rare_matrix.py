def create_rare_matrix(path):
    dim_matrix = 0
    A = {}

    with open(path, 'r+') as f:
        dim_matrix = int(f.readline())
        f.readline()

        for i in range(dim_matrix):
            A[i] = {}

        line = f.readline()

        while line:
            # print(line)

            # preprocessing
            x, i, j = line.split(', ')
            x, i, j = float(x), int(i), int(j)

            # print(x, i, j)
            # print(type(x))

            if j in A[i].keys():
                A[i][j] = A[i][j] + x
            else:
                A[i][j] = x

            line = f.readline()

    return A


def create_tridiag(path):
    """

    :param path:
    :return: (a,b,c) where a  diag pr., b diag. p,  c diag q.
    """

    a = {}
    b = {}
    c = {}

    with open(path, 'r+') as f:
        dim_matrix = int(f.readline())
        p = int(f.readline())
        q = int(f.readline())

        f.readline()
        # print(dim_matrix, p, q)

        for i in range(dim_matrix):
            x = f.readline()
            x = float(x)

            a[f'{i}:{i}'] = x

        f.readline()

        for i in range(dim_matrix - p):
            x = f.readline()
            x = float(x)
            b[f'{i}:{p + i}'] = x

        f.readline()

        for i in range(dim_matrix - q):
            x = float(f.readline())
            c[f'{q + i}:{i}'] = x

    return (0, a), (p, b), (q, c)
