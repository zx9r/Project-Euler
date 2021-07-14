import random
import time
from math import sqrt


def is_prime(n):
    if n == 1:
        return False
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


def miller_rabin(n, k):

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def is_prime_miller(n, k=1):
    return miller_rabin(n, k)


def timer(func):
    def inner(*args, **kargs):
        t1 = time.time()
        f = func(*args, **kargs)
        t2 = time.time()
        print("Runtime took {} seconds".format(t2 - t1))
        return f
    return inner


@timer
def test_function(a, b):
    print(a, b)
    return 0


if __name__ == "__main__":
    print(test_function(1, 2))
    print(is_prime_miller(4))
