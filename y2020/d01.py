from aocd.get import get_day_and_year
from aocd.models import Puzzle

day, year = get_day_and_year()
p = Puzzle(year, day)
print("Day", day, ":", p.title)
data = p.input_data
print(data)

data = [int(num) for num in data.splitlines()]
print(data)

# with open("data.txt", "r") as f:
#     data = f.readlines()

# part 1
for num1 in data:
    for num2 in data:
        if int(num1) + int(num2) == 2020:
            print("Part 1", num1 * num2)

# part 2
for num in data:
    for num2 in data:
        for num3 in data:
            if int(num) + int(num2) + int(num3) == 2020:
                print("Part 2", num * num2 * num3)
