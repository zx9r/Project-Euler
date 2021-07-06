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
