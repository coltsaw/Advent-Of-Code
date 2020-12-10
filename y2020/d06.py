from aocd.get import get_day_and_year
from aocd.models import Puzzle
from collections import defaultdict

day, year = get_day_and_year()
p = Puzzle(year, day)
print("Day", day, ":", p.title)
data = p.input_data
# print(data)

data = [line for line in data.split("\n\n")]
# print(data)

count = 0

for line in data:
    line = line.replace("\n", "")
    s = set()
    for let in line:
        s.add(let)
    count += len(s)

print(count)

count = 0
for line in data:
    group = line.split()
    d = {}
    d = defaultdict(lambda: 0, d)
    for person in group:
        for q in person:
            d[q] += 1

    for key in d:
        if len(group) == d[key]:
            count += 1
print(count)
