from aocd.get import get_day_and_year
from aocd.models import Puzzle

day, year = get_day_and_year()
p = Puzzle(year, day)
print("Day", day, ":", p.title)
data = p.input_data
# print(data)

data = [num for num in data.splitlines()]
# print(data)
x = 0

for each in data:
    char, word = each.split(":")
    # print(char, word)

    first, last = char.split('-')
    last, letter = last.split(' ')
    print(first, last, letter, word, word.count(letter))
    if word.count(letter) >= int(first) and word.count(letter) <= int(last):
        x = x + 1

print(x)

x = 0
for each in data:
    char, word = each.split(":")
    # print(char, word)

    first, last = char.split('-')
    last, letter = last.split(' ')
    print(first, last, letter, word)
    print(word[int(first)])
    print(word[int(last)])
    if (word[int(first)] == letter) ^ (word[int(last)] == letter):
        x = x + 1

    print(x)
