from aocd.get import get_day_and_year
from aocd.models import Puzzle
from collections import defaultdict, Counter

day, year = get_day_and_year()
p = Puzzle(year, day)
print("Day", day, ":", p.title)
data = p.input_data
print(data)

# data = [line for line in data.splitlines()]
# print(data)


def part1():
    pass


def part2():
    pass


part1()
part2()
