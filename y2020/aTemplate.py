from aocd.get import get_day_and_year
from aocd.models import Puzzle

day, year = get_day_and_year()
p = Puzzle(year, day)
print("Day", day, ":", p.title)
data = p.input_data
print(data)

# data = [line for line in data.splitlines()]
# print(data)
