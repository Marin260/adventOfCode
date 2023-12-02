import re

def parseDigit(s: str):
    nums = [c for c in s if c.isdigit()]
    return "".join(nums)

def parseStringDigit(s):
    nums = {
        "one" : "1" ,
        "two" : "2" ,
        "three" : "3" ,
        "four" : "4" ,
        "five" : "5" ,
        "six" : "6" ,
        "seven" : "7" ,
        "eight" : "8" ,
        "nine" : "9" ,
    }

    pattern = "|".join(nums.keys()) + "|\d"

    x = ""
    for i in range(len(s)):
        for match in [re.match(pattern, s[i:])]:
            if match:
                x += nums.get(match.group(),  match.group())
    return x

def calibrate(line: str):
    digitString = parseDigit(line)
    return int(digitString[0] + digitString[-1])

with open("input.txt", "r") as f:
    data = f.read().split("\n")

def partOne(data):
    tot = 0
    for line in data:
        tot += calibrate(line)
    return tot

def partTwo(data):
    tot = 0
    for line in data:
        digit = parseStringDigit(line)
        tot += calibrate(digit)

    return tot

print(partOne(data))
print(partTwo(data))