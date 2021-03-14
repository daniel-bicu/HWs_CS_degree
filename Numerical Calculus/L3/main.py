import rare_matrix
import operations


def bonus():
    A_Triag = rare_matrix.create_tridiag(f'{dir_path}/bonus_a.txt')
    B_Triag = rare_matrix.create_tridiag(f'{dir_path}/bonus_b.txt')

    C_Triag = operations.multiply_triag(A_Triag, B_Triag)
    print('C_Triag')
    operations.display_matrix(C_Triag)


if __name__ == '__main__':
    dir_path = './statics'
    A = rare_matrix.create_rare_matrix(f'{dir_path}/a.txt')
    B = rare_matrix.create_tridiag(f'{dir_path}/b.txt')

    C = operations.add(A, B)
    print('C')
    operations.display_matrix(C)
    C_Good = rare_matrix.create_rare_matrix(f'{dir_path}/aplusb.txt')
    print('Error C', operations.check(C, C_Good), '\n')

    D = operations.multiply(A, B)
    print('D')
    operations.display_matrix(D)
    D_Good = rare_matrix.create_rare_matrix(f'{dir_path}/aorib.txt')
    print('Error D', operations.check(D, D_Good), '\n')

    bonus()