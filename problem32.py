"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1
through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
import timeit
from math import sqrt


def has_repeated_digits(n_str):
    n_str_len = len(n_str)
    for i in range(0, n_str_len - 1):
        for j in range(i + 1, n_str_len):
            if n_str[i] == n_str[j]:
                return True
    return False


def is_pandigital19(n):
    mask = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    while n > 0:
        if n % 10 == 0 or mask[n % 10 - 1] == 1:
            return False
        mask[n % 10 - 1] = 1
        n = n // 10
    return all(mask)  # mask == [1, 1, 1, 1, 1, 1, 1, 1, 1]


start_time = timeit.default_timer()

all_products = set()
for multiplicand in range(1, int(sqrt(987654321)) + 1):
    for multiplier in range(multiplicand + 1, int(sqrt(987654321)) + 1):
        product = multiplicand * multiplier
        pandigital = str(multiplicand) + str(multiplier) + str(product)
        if len(pandigital) < 9:
            continue
        if len(pandigital) > 9:
            break
        if '0' in pandigital:
            continue
        # if has_repeated_digits(pandigital):  -> Different approach, same execution time
        if not is_pandigital19(int(pandigital)):
            continue
        print(multiplicand, multiplier, multiplicand * multiplier)
        all_products.add(product)

print(sorted(all_products))
print(sum(all_products))

print("Elapsed time: {}".format(timeit.default_timer() - start_time))
