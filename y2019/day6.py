inputFile = "inputFiles/day6input.txt"
d = {}


def readLinesIntoDict():
    with open(inputFile, "r") as file:
        for line in file:
            planets = line.strip().split(")")
            obj = planets[0]
            orbiter = planets[1]
            if orbiter not in d:
                d[orbiter] = obj

    # print(d)


def countTotalOrbits(key):
    count = 1

    if d[key] in d:
        count += countTotalOrbits(d[key])

    return count


def getObjList(key):
    objList = []
    if d[key] in d:
        objList.append(d[key])
        objList += getObjList(d[key])

    return objList


def findIntersect(YOUlist, SANlist):
    for i in YOUlist:
        for j in SANlist:
            if (i == j):
                return i


def calcDistance(YOUlist, SANlist):
    count = 0
    intersect = findIntersect(YOUlist, SANlist)

    i = 0
    while YOUlist[i] != intersect:
        count += 1
        i += 1

    i = 0
    while SANlist[i] != intersect:
        count += 1
        i += 1

    return count


def part1():
    count = 0
    for key in d:
        count += countTotalOrbits(key)

    return count


def part2():
    count = 0
    YOUlist = getObjList('YOU')
    SANlist = getObjList('SAN')

    count = calcDistance(YOUlist, SANlist)

    return count


if __name__ == "__main__":
    readLinesIntoDict()

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
