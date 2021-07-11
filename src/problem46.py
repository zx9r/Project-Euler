"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and
twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
from src.utils import timer, is_prime


def goldbach_numbers(n):
    i = 1
    s = 2 * i**2
    while s < n:
        if is_prime(n - s):
            return n - s, i
        i += 1
        s = 2 * i ** 2
    return 0, 0


@timer
def problem46():
    result = 7
    found = False
    while not found:
        result += 2
        if is_prime(result):
            continue
        p, s = goldbach_numbers(result)
        print("{} = {} + 2 * {}^2".format(result, p, s))
        if (p, s) == (0, 0):
            found = True

    return result


if __name__ == "__main__":
    # 5777
    print(problem46())
