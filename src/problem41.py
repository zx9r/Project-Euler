"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
from functools import reduce
from itertools import permutations

from src.utils import timer, is_prime


@timer
def problem41():
    digits = [i for i in range(9, 0, -1)]
    while True:
        for pandigital in permutations(digits):
            pand_number = reduce(lambda x, y: 10*x+y, pandigital)
            if is_prime(pand_number):
                return pand_number
        digits = digits[1:]


if __name__ == "__main__":
    print("Solution: {}".format(problem41()))
