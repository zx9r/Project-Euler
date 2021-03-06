"""
Pentagonal numbers are generated by the formula, Pn=n(3nā1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 ā 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk ā Pj|
is minimised; what is the value of D?
"""
from math import sqrt

from src.utils import timer


def is_pentagonal(p):
    # p = n(3nā1)/2 ->
    n = (1 + sqrt(1 + 24 * p)) / 6
    return n.is_integer()


@timer
def problem44():
    result = 0
    pentagonals = []
    found = False
    n = 0
    while not found:
        n += 1
        p1 = n * (3 * n - 1) // 2
        for p2 in pentagonals:        
            if is_pentagonal(p1 + p2) and is_pentagonal(p1 - p2):
                found = True
                result = p1 - p2
                break
        pentagonals.append(p1)

    return result


if __name__ == "__main__":
    # 5482660
    print(problem44())
