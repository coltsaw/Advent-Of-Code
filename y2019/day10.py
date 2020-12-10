

inputFile = "inputFiles/day10input.txt"


def readInput():
    x = 0
    y = 0
    asteroids = set()
    with open(inputFile, 'r') as input:
        for row in input:
            for i in range(len(row)):
                if row[i] == "#":
                    x = i
                    asteroids.add(complex(x, y))
            y += 1

    print(asteroids)
    return asteroids


def createSeenDict(asteroids):
    numSeen = {}
    for a in asteroids:
        numSeen[a] = 0
        for b in asteroids:
            if a != b:
                slope, b = calculateLineBetweenPonts(a, b)
                blocked = False
                for c in asteroids:
                    if c.real > a.real and c.real < b.real:
                        if c.imag == slope * c.real + b:
                            blocked = True
                if blocked == False:
                    numSeen[a] += 1

    return numSeen


def calculateLineBetweenPonts(pointA, pointB):
    slope = calculateSlope(pointA, pointB)
    b = pointA.imag - slope * pointA.real

    return slope, b


def calculateSlope(pointA, pointB):
    if (pointA.real == pointB.real):
        return 0
    else:
        return (pointB.imag - pointA.imag) / (pointB.real - pointA.real)


def part1():
    asteroids = readInput()
    seenDict = createSeenDict(asteroids)
    print(seenDict)


def part2():
    return


if __name__ == "__main__":

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
