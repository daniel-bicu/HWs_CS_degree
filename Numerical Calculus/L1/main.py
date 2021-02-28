import datetime
import math
from random import random, randrange
from random import seed
import matplotlib.pyplot as plt

import matplotlib as matplotlib
import numpy as np

from pregatire_input_tan import reducere_interval, reducere_interval_MacLaurin
from random import uniform


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
    semn, x = reducere_interval(x)

    if x % (math.pi / 2) == 0:
        if semn == -1:
            return '-infinit'
        else:
            return '+infinit'

    a = x
    b = 0
    f = b

    if f == 0:
        f = CONST_MIC

    C = f
    D = 0
    b = 1
    # executam o iteratie inainte

    D = b + a * D
    if D == 0:
        D = CONST_MIC

    C = b + a / C

    if C == 0:
        C = CONST_MIC

    D = 1 / D
    delta = C * D
    f = delta * f

    # pentru urmatoarele iteratii avem
    # b va fi mereu +=2 (val impare)
    # a va fi mereu - x^2

    a = -x ** 2

    while math.fabs(delta - 1) >= epsilon:
        b += 2
        D = b + a * D
        if D == 0:
            D = CONST_MIC
        C = b + a / C

        if C == 0:
            C = CONST_MIC

        D = 1 / D
        delta = C * D
        f = delta * f

    return semn * f


def my_tan_2(x):
    c0, c1, c2, c3, c4 = 1, 1 / 3, 2 / 15, 17 / 315, 62 / 2835

    exponent, semn, x = reducere_interval_MacLaurin(x)

    if x % (math.pi / 2) == 0:
        if semn == -1:
            return '-infinit'
        else:
            return '+infinit'

    x_3, x_5, x_7, x_9 = x ** 3, x ** 5, x ** 7, x ** 9

    result = c0 * x + c1 * x_3 + c2 * x_5 + c3 * x_7 + c4 * x_9

    return semn * (result ** exponent)


def error_tan(fct, lista):
    start_time = datetime.datetime.now()

    mean_error = 0
    times = []
    values = []

    for item in lista:
        value = math.fabs(math.tan(item) - fct(item))
        mean_error += value

        time_diff = (datetime.datetime.now() - start_time)
        execution_time = time_diff.total_seconds() * 1000
        times.append(execution_time)
        values.append(value)

    end_time = datetime.datetime.now()

    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000

    return mean_error / 10_000, execution_time, times, values


def exercitiul_3():
    numbers = [uniform(-math.pi / 2, math.pi / 2) for i in range(10_000)]

    f = open('results_tan.txt', 'w+')

    result_my_tan_1, time_my_tan_1, times_my_tan_1, values_my_tan_1 = error_tan(my_tan_1, numbers)
    result_my_tan_2, time_my_tan_2, times_my_tan_2, values_my_tan_2 = error_tan(my_tan_2, numbers)

    f.write(f'Meth.continous fractions: {result_my_tan_1} with time: {time_my_tan_1}\n'
            f'Meth. MacLaurin: {result_my_tan_2} with time: {time_my_tan_2}.')

    times_my_tan_1 = np.array(times_my_tan_1)
    times_my_tan_1 = times_my_tan_1.reshape(100, 100).mean(axis=1)

    values_my_tan_1 = np.array(values_my_tan_1)
    values_my_tan_1 = values_my_tan_1.reshape(100, 100).mean(axis=1)

    fig = plt.figure(figsize=(10, 8))
    plt.plot(times_my_tan_1, values_my_tan_1, 'o', ls='-', ms=4, markevery=0.1, color='lightblue', linewidth=1)
    plt.xlabel('time')
    plt.ylabel('error')
    fig.savefig("tan_1.pdf", bbox_inches='tight')

    times_my_tan_2 = np.array(times_my_tan_2)
    times_my_tan_2 = times_my_tan_2.reshape(100, 100).mean(axis=1)

    values_my_tan_2 = np.array(values_my_tan_2)
    values_my_tan_2 = values_my_tan_2.reshape(100, 100).mean(axis=1)

    fig = plt.figure(figsize=(10, 8))
    plt.plot(times_my_tan_2, values_my_tan_2, 'o', ls='-', ms=4, markevery=0.1, color='lightblue', linewidth=1)
    plt.xlabel('time')
    plt.ylabel('error')
    fig.savefig("tan_2.pdf", bbox_inches='tight')

    fig = plt.figure(figsize=(10, 8))
    plt.plot(times_my_tan_1, values_my_tan_1, 'o', label='my_tan_1', ls='-', ms=4, markevery=0.1, color='blue',
             linewidth=1)
    plt.plot(times_my_tan_2, values_my_tan_2, 'o', label='my_tan_2', ls='-', ms=4, markevery=0.1, color='red',
             linewidth=1)
    plt.xlabel('time')
    plt.ylabel('error')
    fig.savefig("tan.pdf", bbox_inches='tight')


if __name__ == '__main__':
    precizia_masina = exercitiul_1()
    print('Precizia masina', precizia_masina)
    # calculam u-ul

    u = 10 ** (-precizia_masina)

    print('Este adunarea asociativa? ', exercitiul_2_adunare(1.0, u / 10, u / 10))
    print('3 Numere pentru care inmultirea nu este asociativa: ', exercitiul_2_inmultire())

    print('Tan  - din biblioteca de matematica: ', math.tan(48))
    print('Tan1 - meth. fractiilor continue: ', my_tan_1(48))
    print('Tan2 - meth. polinoamelor: ', my_tan_2(48))

    exercitiul_3()
