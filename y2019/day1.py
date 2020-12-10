import math

inputFile = "inputFiles/day1input.txt"


def findTotalFuel():
    fuel = 0
    with open(inputFile, 'r') as input:
        for data in input:
            fuel += calcFuel(int(data))

    return fuel


def findTotalFuelWithFuel():
    fuel = 0
    with open(inputFile, 'r') as input:
        for data in input:
            fuel += calcFuel(int(data))
            fuel += findFuelForFuel(calcFuel(int(data)))

    return fuel


def findFuelForFuel(num):
    fuel = 0
    fuelForFuel = calcFuel(num)
    while (fuelForFuel >= 0):
        fuel += fuelForFuel
        fuelForFuel = calcFuel(fuelForFuel)

    return fuel


def calcFuel(num):
    return math.floor(num / 3) - 2


def part1():
    return findTotalFuel()


def part2():
    return findTotalFuelWithFuel()


if __name__ == "__main__":

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
