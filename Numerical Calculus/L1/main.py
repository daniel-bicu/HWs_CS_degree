import math
from random import random
from random import seed
from pregatire_input_tan import reducere_interval


# ex 1

def exercitiul_1(m=1):
    """
    precizia masina = acea valoare pentru care calculatorul il va aproxima ca 0
    :param m: de unde dorim sa plecam cu cautarea, default: 1
    :return: precizia masina
    """

    u = 10 ** (-m)
    conditie = True if 1.0 + u != 1.0 else False
    while conditie:
        m += 1
        u /= 10
        conditie = True if 1.0 + u != 1.0 else False

    return m - 1


def exercitiul_2_adunare(a, b, c):
    """
    Dorim sa verificam asociativitatea adunarii efectuata de un calculator, in contextul in care avem ca si membrii
    adunarii urmatorii:
    :param a:  a = 1.0
    :param b:  b = u/10, unde u reprezinta precizia_masina
    :param c:  c = u/10, analog b
    :return:   True - daca asociativatea este indeplinita, False altfel.
    """
    return (a + b) + c == a + (b + c)


def exercitiul_2_inmultire():
    """
    Dorim sa gasim 3 parametrii: a, b, c a.i
    :return: un triplet (a,b,c) (i.e. tupla) a.i. (a*b)*c <> a*(b*c)
    """
    f = open('results.txt', 'w+')

    # seed(1)
    a = random()
    b = random()
    c = random()
    conditie = True if (a * b) * c == a * (b * c) else False

    if not conditie:
        result1 = (a * b) * c
        result2 = a * (b * c)

        result = f'{a}, {b}, {c} unde:\n (a*b)*c = {result1}, \n iar a*(b*c) = {result2}.'
        f.write(result)
        return a, b, c

    while conditie:
        a = random()
        b = random()
        c = random()

        conditie = True if (a * b) * c == a * (b * c) else False

        if not conditie:
            result1 = (a * b) * c
            result2 = a * (b * c)

            result = f'{a}, {b}, {c} unde:\n (a*b)*c = {result1}, \n iar a*(b*c) = {result2}.'
            f.write(result)

    return a, b, c


CONST_MIC = 10 ** (-12)


def my_tan_1(x, epsilon=10 ** (-12)):
    x = reducere_interval(x)[1]

    a = x
    b0 = 0

    f = b0

    if f == 0:
        f0 = CONST_MIC

    C = b0
    D = 0
    b = 1
    # executam o iteratie inainte

    D = b + a * D
    if D == 0:
        D = CONST_MIC

    if C == 0:
        C = CONST_MIC

    C = b + a / C

    if C == 0:
        C = CONST_MIC

    D = 1 / D
    delta = C * D
    f = delta * f;

    # pentru urmatoarele iteratii avem
    # b va fi mereu +=2 (val impare)
    # a va fi mereu - x^2

    a = - x ** 2

    while delta - 1 >= epsilon:
        b += 2
        D = b + a * D
        if D == 0:
            D = CONST_MIC
        C = b + a / C

        if C == 0:
            C = CONST_MIC

        D = 1 / D
        delta = C * D
        f = delta * f;

    return f


def exercitiul_3():
    pass


if __name__ == '__main__':
    precizia_masina = exercitiul_1()
    print(precizia_masina)
    # calculam u-ul

    u = 10 ** (-precizia_masina)

    print(exercitiul_2_adunare(1.0, u / 10, u / 10))
    print(exercitiul_2_inmultire())

    print('Tan from math', math.tan(45))
    print('Tan1', my_tan_1(45))
