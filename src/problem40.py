"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000"""
from functools import reduce

from src.utils import timer


@timer
def problem40():
    sequence = ""
    n = 0
    while len(sequence) <= 1_000_000:
        sequence += str(n)
        n += 1
    print(sequence[:100])
    digits = [int(sequence[10**i]) for i in range(0, 7)]
    print(digits)
    return reduce(lambda x, y: x * y, digits)


if __name__ == "__main__":
    print("Solution: {}".format(problem40()))
