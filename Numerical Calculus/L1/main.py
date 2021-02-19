import math


# ex 1

def exercitiul_1(m):
    """
    precizia masina = acea valoare pentru care calculatorul il va aproxima ca 0
    :param m: de unde dorim sa plecam cu cautarea
    :return: precizia masina
    """

    u = 10 ** (-m)
    conditie = True if 1.0 + u != 1.0 else False
    while conditie:
        m += 1
        u /= 10
        conditie = True if 1.0 + u != 1.0 else False

    return m - 1


def exercitiul_2(m):
    pass


if __name__ == '__main__':
    precizia_masina = exercitiul_1(1)

    # calculam u-ul

    u = 10 ** (-precizia_masina)

    print(u)
