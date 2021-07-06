"""
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


sum_of_squares_first100 = sum([n**2 for n in range(1, 101)])
square_of_sum_first100 = sum(range(1, 101))**2

print(square_of_sum_first100 - sum_of_squares_first100)
