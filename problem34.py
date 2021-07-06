"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
import math

solution = 0
for i in range(10, 100000):
    i2 = i
    sum_fact_digits = 0
    while i2 > 0:
        sum_fact_digits += math.factorial(i2 % 10)
        i2 = i2 // 10
    if sum_fact_digits == i:
        print(i)
        solution += i

print("Solution: {}".format(solution))
