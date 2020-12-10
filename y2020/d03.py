from aocd.get import get_day_and_year
from aocd.models import Puzzle

day, year = get_day_and_year()
p = Puzzle(year, day)
print("Day", day, ":", p.title)
data = p.input_data
# print(data)

data = [line for line in data.splitlines()]
# print(data)


def slopes(dx, dy):
    y = 0
    x = 0
    count = 0
    limit = len(data[0])

    while (y < len(data)):
        if x >= limit:
            x = x-limit
        # print(data[x])
        # print(data[x][y])
        if data[y][x] == "#":
            count += 1
        x += dx
        y += dy

    return count


print(slopes(3, 1))

print(slopes(1, 1) * slopes(3, 1) * slopes(5, 1) * slopes(7, 1) * slopes(1, 2))
