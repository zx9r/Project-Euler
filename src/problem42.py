"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""
from src.utils import timer


@timer
def problem42():
    triangle_numbers = [n * (n + 1) // 2 for n in range(1, 1000)]
    triangle_words = 0
    with open("p042_words.txt", "r") as f:
        words = f.readline().split(",")
        words = [word[1:-1] for word in words]
        for word in words:
            word_value = sum([ord(letter) - ord("A") + 1 for letter in word])
            if word_value in triangle_numbers:
                triangle_words += 1
    return triangle_words


if __name__ == '__main__':
    print("Solution: {}".format(problem42()))
