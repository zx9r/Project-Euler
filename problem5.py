"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import timeit

start_time = timeit.default_timer()

n = 20
found = False
while not found:
    found = True
    n += 20
    for d in range(19, 10, -1):
        if n % d != 0:
            found = False
            break

# Solution is 232792560
print(n)

print("Elapsed time: {}".format(timeit.default_timer() - start_time))
