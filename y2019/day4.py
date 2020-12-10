start = 245182
end = 790572


def checkIfIncrement(numStr):
    for i in range(5):
        if (numStr[i] > numStr[i + 1]):
            return False

    return True


def checkDoubleDigit(numStr):
    for i in range(5):
        if (numStr[i] == numStr[i + 1]):
            return True

    return False


def checkOnlyTwoDigits(numStr):
    for i in range(5):
        if (numStr[i] == numStr[i + 1] and numStr.count(numStr[i]) == 2):
            return True

    return False


def solve(func):
    count = 0

    for num in range(start, end):
        curStr = str(num)
        if (checkIfIncrement(curStr) and func(curStr)):
            count += 1

    return count


def part1():
    return solve(checkDoubleDigit)


def part2():
    return solve(checkOnlyTwoDigits)


if __name__ == "__main__":

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
