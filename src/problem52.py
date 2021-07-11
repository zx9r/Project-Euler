"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
from src.utils import timer, is_prime


@timer
def problem52():
    multipliers = range(2, 7)
    x = 1
    while True:
        if all([sorted(str(x)) == sorted(str(x * m)) for m in multipliers]):
            print(x, [x * m for m in multipliers])
            return x
        x += 1


@timer
def problem52_2():
    multipliers = range(2, 7)
    x = 0
    found = False
    while not found:
        x += 1
        found = True
        for m in multipliers:
            if sorted(str(x)) != sorted(str(x * m)):
                found = False
                break
    print(x, [x * m for m in multipliers])
    return x


if __name__ == "__main__":
    # 142857
    print(problem52())
    print(problem52_2())
