"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000
"""
from src.utils import timer


@timer
def problem48():
    modulus = 10_000_000_000
    result = 0
    for i in range(1, 1001):
        result += pow(i, i, modulus)
    return result % modulus


if __name__ == "__main__":
    # 9110846700
    print(problem48())
