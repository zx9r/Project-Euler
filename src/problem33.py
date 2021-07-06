"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits
in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""


fractions_product = [1, 1]
for numerator in range(10, 99):
    for denominator in range(numerator + 1, 100):
        if numerator % 10 == denominator % 10 == 0:
            continue
        a, b = str(numerator)
        c, d = str(denominator)
        if a == c:
            a = c = ""
        if a == d:
            a = d = ""
        if b == c:
            b = c = ""
        if b == d:
            b = d = ""
        if a + b == "":
            continue
        new_numerator = int(a + b)
        new_denominator = int(c + d)
        if numerator != new_numerator and new_denominator != 0\
                and numerator / denominator == new_numerator / new_denominator:
            print("{}/{} -> {}/{}".format(numerator, denominator, new_numerator, new_denominator))
            fractions_product[0] *= new_numerator
            fractions_product[1] *= new_denominator

print(fractions_product)
