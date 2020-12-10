from aocd.get import get_day_and_year
from aocd.models import Puzzle

day, year = get_day_and_year()
p = Puzzle(year, day)
print("Day", day, ":", p.title)
data = p.input_data
# print(data)

data = [line for line in data.splitlines()]
# print(data)

# data = ["FBFBBFFRLR"]


def get_row(line):
    line = line[0:7]
    # print(line)

    lower = 0
    upper = 127
    for c in line:
        num = (upper - lower) // 2 + 1
        # print(num, lower, upper)
        if c == "F":
            upper -= num
        if c == "B":
            lower += num
    return upper


def get_column(line):
    line = line[7:]
    # print(line)

    lower = 0
    upper = 7
    for c in line:
        num = (upper - lower) // 2 + 1
        # print(num, lower, upper)
        if c == "L":
            upper -= num
        if c == "R":
            lower += num
    return upper


seats = []

highest = 0
for line in data:
    row = get_row(line)
    col = get_column(line)
    seat_id = row * 8 + col
    seats.append(seat_id)
    if seat_id > highest:
        highest = seat_id

# part 1
print(highest)

# part 2
seats.sort()
print(seats)

for i in range(highest + 1):
    if i not in seats:
        print(i)
