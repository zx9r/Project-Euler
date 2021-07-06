"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import timeit


def calculate_sequence_elements_total(d: dict, n: int) -> int:
    if d.get(n, -1) != -1:
        return d.get(n)
    result = 0
    while n > 1:
        if d.get(n, -1) != -1:
            result += d.get(n)
            return result
        result += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1

    result += 1
    return result


start_time = timeit.default_timer()

longest = 0
calculated = {}
for i in range(1, 1000000):
    num_elements = calculate_sequence_elements_total(calculated, i)
    calculated[i] = num_elements
    if num_elements > longest:
        longest = num_elements
        print("{} -> {}".format(i, longest))

# solution is 837799 (525 elements)
print("Elapsed time: {}".format(timeit.default_timer() - start_time))