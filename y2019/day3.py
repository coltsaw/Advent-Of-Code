
inputFile = "inputFiles/day3input.txt"


def readInput():
    with open(inputFile, 'r') as input:
        wire1cmd, wire2cmd = input.readlines()
        wire1cmd = wire1cmd.strip().split(',')
        wire2cmd = wire2cmd.strip().split(',')

    return wire1cmd, wire2cmd


def createSet(commands):
    x = 0
    y = 0
    save = complex(x, y)
    wireSet = {save}
    for cmd in commands:
        x = save.real
        y = save.imag
        if cmd[0] == "U":
            for i in range(int(cmd[1:])):
                y += 1
                wireSet.add(complex(x, y))
            save = complex(x, y)
        elif cmd[0] == "R":
            for i in range(int(cmd[1:])):
                x += 1
                wireSet.add(complex(x, y))
            save = complex(x, y)
        elif cmd[0] == "D":
            for i in range(int(cmd[1:])):
                y -= 1
                wireSet.add(complex(x, y))
            save = complex(x, y)
        elif cmd[0] == "L":
            for i in range(int(cmd[1:])):
                x -= 1
                wireSet.add(complex(x, y))
            save = complex(x, y)

    return wireSet


def checkIntersection(wire1, wire2):
    intersect = set()
    for point in wire1:
        if point in wire2:
            intersect.add(point)

    intersect.remove(0j)
    return intersect


def calcClosestToOrigin(intersectionSet):
    start = intersectionSet.pop()
    dist = abs(start.real) + abs(start.imag)
    for point in intersectionSet:
        if abs(point.real) + abs(point.imag) < dist:
            dist = abs(point.real) + abs(point.imag)

    return int(dist)


def part1():
    wire1cmd, wire2cmd = readInput()
    wire1points = createSet(wire1cmd)
    wire2points = createSet(wire2cmd)
    # print(wire1points)
    # print(wire2points)

    intersections = checkIntersection(wire1points, wire2points)
    # print(intersections)

    return calcClosestToOrigin(intersections)


def part2():
    return


if __name__ == "__main__":

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
