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
