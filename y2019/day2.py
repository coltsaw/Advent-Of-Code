import time

inputFile = "inputFiles/day2input.txt"
p2output = 19690720


def readInput():
    with open(inputFile, 'r') as input:
        for line in input:
            array = line.strip().split(',')

    for i in range(len(array)):
        array[i] = int(array[i])

    # print(array)
    return array


def calculate(code, num1, num2):
    if (code == 1):
        return num1 + num2
    if (code == 2):
        return num1 * num2
    if (code == 99):
        return (-1)

    return code


def part1():
    array = readInput()
    array[1] = 12
    array[2] = 2
    i = 0
    while i < len(array) and array[i] != 99:
        output = calculate(
            array[i], array[array[i + 1]], array[array[i + 2]])
        array[array[i + 3]] = output
        i += 4
    return array[0]


def part2():
    output = 0
    for j in range(100):
        for k in range(100):
            if (output <= p2output):
                array = readInput()
                array[1] = j
                array[2] = k
                i = 0
                while i < len(array) and array[i] != 99:
                    output = calculate(
                        array[i], array[array[i + 1]], array[array[i + 2]])
                    array[array[i + 3]] = output
                    i += 4

    return 100 * array[1] + array[2] - 1


if __name__ == "__main__":
    start = time.time()
    print(f"Part 1: {part1()}")
    mid = time.time()
    print(f"Part 2: {part2()}")
    end = time.time()

    print(end - start)
    print(mid - start)
    print(end - mid)
