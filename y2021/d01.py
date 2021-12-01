from aocd.get import get_day_and_year
from aocd.models import Puzzle
from collections import defaultdict, Counter

day, year = get_day_and_year()
p = Puzzle(year, day)
print("Day", day, ":", p.title)
data = p.input_data
print(data)

data = [line for line in data.splitlines()]
print(data)


def part1():
    count = 0
    for i in range(len(data)):
        if int(data[i]) > int(data[i - 1]):
            count = count + 1

    print(count)


def part2():
    count = 0
    for i in range(len(data) - 2):
        if int(data[i]) + int(data[i + 1]) + int(data[i + 2]) > int(data[i - 1]) + int(data[i]) + int(data[i + 1]):
            count += 1

    print(count)


part1()
part2()
