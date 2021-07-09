"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product
of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer
with (1,2, ... , n) where n > 1?
"""

def try_pandigital(p):
    '''
    Tries if is it possible to create a 1 to 9 pandigital number by concatenating the product of p with (1,2,...n)
    where n > 1
    :param p:
    :return: a 1 to 9 pandigital number if possible, 0 otherwise
    '''
    pandigital = str(p)
    n = 2
    while len(pandigital) < 9:
        pandigital += str(p * n)
        n += 1
    if len(pandigital) > 9:
        return 0
    return int(pandigital) if "".join(sorted(pandigital)) == "123456789" else 0


for i in range(99999):
    p = try_pandigital(i)
    if p:
        print("{} generates {}".format(i, p))
