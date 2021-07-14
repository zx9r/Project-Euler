"""
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one
followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""
from src.utils import timer


@timer
def problem56():
    result = 0
    for a in range(2, 100):
        for b in range(2, 100):
            p = a**b
            digits_sum = 0
            while p > 0:
                digits_sum += p % 10
                p = p // 10
            if digits_sum > result:
                result = digits_sum
    return result


if __name__ == "__main__":
    print(problem56())
