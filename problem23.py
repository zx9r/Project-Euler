"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import timeit
from math import sqrt


def divisors_sum(n):
    result = 1
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            result += i
            if (n / i) != i:
                result += n // i

    return result


start_time = timeit.default_timer()

abundant_numbers = []
for i in range(1, 28124):
    if divisors_sum(i) > i:
        abundant_numbers.append(i)

# print(abundant_numbers)

#sum_of_2_abundant_numbers = set()
sum_of_2_abundant_numbers = [0] * 60000
for i in abundant_numbers:
    for j in abundant_numbers:
        #sum_of_2_abundant_numbers.add(i + j)
        sum_of_2_abundant_numbers[i + j] = 1

total = 0
for i in range(1, 28124):
    #if i not in sum_of_2_abundant_numbers:
    if sum_of_2_abundant_numbers[i] == 0:
        total += i

print(total)  # Solution is 4179871

print("Elapsed time: {}".format(timeit.default_timer() - start_time))
