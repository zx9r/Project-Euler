"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from math import sqrt


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    result = True
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            result = False
            break
    return result


n = 1  # Will not check for prime 2
p = 1  # Will start search at 3
while n < 10001:
    p += 2
    if is_prime(p):
        n += 1

# Solution is 104743
print(p)
