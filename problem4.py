"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import timeit


def is_palindrome(n: int) -> bool:
    n_str = str(n)
    return n_str == n_str[::-1]


def search_largest_palindrome():
    n1 = n2 = prod_n1n2 = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            prod_ij = i*j
            n_str = str(prod_ij)
            #if is_palindrome(i * j) and i * j > n1 * n2:
            if n_str == n_str[::-1] and prod_ij > prod_n1n2:
                n1, n2 = i, j
                prod_n1n2 = prod_ij
    return n1, n2




start_time = timeit.default_timer()

n1, n2 = search_largest_palindrome()
print("{} = {} * {}".format(n1 * n2, n1, n2))

print("Elapsed time: {}".format(timeit.default_timer() - start_time))
