"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
left to right, and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from utils import is_prime

solution = 0
for i in range(11, 1000000, 2):
    valid = True
    for j in range(len(str(i))):
        trunc_left = int(str(i)[:j+1])
        trunc_right = int(str(i)[j:])
        if not is_prime(trunc_left) or not is_prime(trunc_right):
            valid = False
            break
    if valid:
        print(i)
        solution += i

print("Solution: {}".format(solution))
