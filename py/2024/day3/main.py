import re

with open("./input.txt", "r") as f:
    data = f.read()

matches = re.findall("mul\(\d{1,3},\d{1,3}[)]", data)

tot1 = 0
for el in matches:
    l, r = el[4:-1].split(",")
    tot1 += int(l) * int(r)

matches2 = re.findall("mul\(\d{1,3},\d{1,3}[)]|do\(\)|don't\(\)", data)

tot2 = 0
go = True
for el in matches2:
    if el == "do()":
        go = True
    elif el == "don't()":
        go = False
    else:
        if go is True:
            l, r = el[4:-1].split(",")
            tot2 += int(l) * int(r)

print(tot2)
