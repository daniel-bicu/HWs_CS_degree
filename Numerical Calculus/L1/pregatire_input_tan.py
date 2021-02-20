__doc__ = "Pregatire input tangenta"

import math


def antisimetrie(x):
    if x < 0:
        return -1, -x

    return 1, x


def periodicitate(x):
    return x % math.pi


def reducere_interval(x):
    x = periodicitate(x)

    semn, x = antisimetrie(x)

    return semn, x


def reducere_interval_MacLaurin(x):
    semn, x = reducere_interval(x)

    x = math.pi/2 - x

    return -1, semn, x