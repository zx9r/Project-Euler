"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""
from math import sqrt

from src.utils import timer


def calculate_factors(n):
    result = set()
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            result.add(2)
            continue
        possible_prime = True
        for f in range(3, int(sqrt(n)) + 1, 2):
            if n % f == 0:
                possible_prime = False
                n = n // f
                result.add(f)
                break
        if possible_prime:
            result.add(n)
            break

    return result


@timer
def problem47():
    consecutives = 4
    lasttry_factors = [calculate_factors(i) for i in range(2, consecutives + 2)]
    i = consecutives + 2
    result = 0
    while result == 0:
        lasttry_factors[i % consecutives] = calculate_factors(i)
        # print(lasttry_factors)
        combined = [factor for s in lasttry_factors for factor in s]
        if len(combined) // consecutives == consecutives and all([len(f) == consecutives for f in lasttry_factors]):
            result = i - consecutives + 1
        else:
            i += 1
    return result


if __name__ == "__main__":
    # 134043
    print(problem47())
