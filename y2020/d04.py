from aocd.get import get_day_and_year
from aocd.models import Puzzle
import re

day, year = get_day_and_year()
p = Puzzle(year, day)
print("Day", day, ":", p.title)
data = p.input_data
# print(data)

# data = """eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946

# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007"""
data = [line for line in data.split("\n\n")]
# print(data)

valids = ["byr",
          "iyr",
          "eyr",
          "hgt",
          "hcl",
          "ecl",
          "pid"]

count = 0
count2 = 0


def check_valid(passport: dict):
    for y in valids:
        if y not in passport:
            return 0
    return 1


def check_byr(byr):
    return len(byr) == 4 and int(byr) in range(1920, 2002 + 1)


def check_iyr(iyr):
    return len(iyr) == 4 and int(iyr) in range(2010, 2020 + 1)


def check_eyr(eyr):
    return len(eyr) == 4 and int(eyr) in range(2020, 2030 + 1)


def check_hgt(hgt):
    sys = hgt[len(hgt) - 2:]
    hgt = hgt[0:-2]
    # print(hgt)
    if sys == "cm":
        return int(hgt) in range(150, 193 + 1)
    elif sys == "in":
        return int(hgt) in range(59, 76 + 1)
    else:
        return False


def check_hcl(hcl):
    reg = re.compile(r"^#[0-9a-f]{6}$")
    return re.match(reg, hcl) is not None


def check_ecl(ecl):
    colors = "amb blu brn gry grn hzl oth".split(' ')
    return ecl in colors


def check_pid(pid):
    reg = re.compile(r"^[0-9]{9}$")
    print(re.match(reg, pid))
    return re.match(reg, pid) is not None


def check_passport(passport: dict):
    byr = passport.get("byr")
    iyr = passport.get("iyr")
    eyr = passport.get("eyr")
    hgt = passport.get("hgt")
    hcl = passport.get("hcl")
    ecl = passport.get("ecl")
    pid = passport.get("pid")

    print(passport)
    print(check_byr(byr), check_iyr(iyr), check_eyr(eyr), check_hgt(
        hgt), check_hcl(hcl), check_ecl(ecl), check_pid(pid))
    return check_byr(byr) and check_iyr(iyr) and check_eyr(eyr) and check_hgt(hgt) and check_hcl(hcl) and check_ecl(ecl) and check_pid(pid)


for each in data:
    each = each.replace("\n", " ")
    each = each.split(" ")
    props = {}
    for x in each:
        item, value = x.split(":")
        props[item] = value

    # print(props)
    count += check_valid(props)  # Part 1

    # Part 2
    if check_valid(props) == 1 and check_passport(props):
        count2 += 1

print(count)
print(count2)
