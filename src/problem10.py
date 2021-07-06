"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import utils

primes_sum = 2
for i in range(3, 2000000, 2):
    if utils.is_prime(i):
        primes_sum += i

print(primes_sum)
