"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three
solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
import timeit

start_time = timeit.default_timer()

perimeter_value = 0
max_solutions = 0
for p in range(1, 1001):
    solutions = 0
    for a in range(1, p // 3):
        for b in range(a, p - a):
            c = p - a - b
            if c <= b:
                break
            if (a**2 + b**2) != c**2:
                continue
            solutions += 1
        if solutions > max_solutions:
            max_solutions = solutions
            perimeter_value = p

# 840
print(perimeter_value)

print("Elapsed time: {}".format(timeit.default_timer() - start_time))
