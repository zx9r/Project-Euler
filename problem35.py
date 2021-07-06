"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719,
are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from utils import is_prime

num_circular_primes = 1  # Initialization to 1 because number 2 is prime and not testing in the loop
for i in range(3, 1000000, 2):
    i_str = str(i)
    circular_prime = True
    for _ in range(0, len(str(i))):
        if not is_prime(int(i_str)):
            circular_prime = False
            break
        i_str = i_str[1:] + i_str[0]
    if circular_prime:
        print(i)
        num_circular_primes += 1

print("Solution: {}".format(num_circular_primes))


