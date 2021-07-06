"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""


def name_score(name):
    result = 0
    for c in name:
        result += ord(c) - ord('A') + 1
    return result


with open("p022_names.txt", "r") as names_file:
    names = names_file.readline()

names = [name[1:-1] for name in names.split(",")]
names = sorted(names)

total = 0
for i in range(0, len(names)):
    total += (i + 1) * name_score(names[i])

print(total)
