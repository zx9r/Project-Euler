"""
https://projecteuler.net/problem=55
"""
from src.utils import timer


def is_lychrel(n):
    for _ in range(50):
        n = n + int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
    return True


@timer
def problem55():
    result = 0
    for i in range(10_000):
        if is_lychrel(i):
            result += 1
    return result


if __name__ == "__main__":
    print(problem55())
