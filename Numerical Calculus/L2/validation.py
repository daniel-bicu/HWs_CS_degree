import numpy as np


def validate_for_cholesky(matrix):
    matrix = np.array(matrix)
    det = np.linalg.det(matrix)

    if (matrix == matrix.transpose()).all() and det != 0:
        return True
    return False


if __name__ == '__main__':
    matrix = [
            [1, 0, 3],
            [0, 4, 2],
            [3, 2, 11]
        ]

    result = validate_for_cholesky(matrix)
    print(result)
