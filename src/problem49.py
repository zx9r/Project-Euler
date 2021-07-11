"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is
one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
from src.utils import timer, is_prime


@timer
def problem49():
    start = 1239
    for i in range(start, 10000):
        if not is_prime(i):
            continue
        a = sorted(str(i))
        for j in range(1, (10000 - i) // 2 + 1):
            b = i + j
            if not is_prime(b):
                continue
            c = i + 2 * j
            if not is_prime(c):
                continue
            if a == sorted(str(b)) and a == sorted(str(c)):
                print(i, i + j, i + 2 * j, j)
                if i != 1487:
                    return str(i) + str(b) + str(c)


if __name__ == "__main__":
    print(problem49())
