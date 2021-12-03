# Part one
with open('day2/input.txt') as f:
    scans = f.readlines()

hValue = 0
dValue = 0
for i in range(len(scans)):
    scans[i]= scans[i].split()
    if scans[i][0] == "forward":
        hValue += int(scans[i][1])
    elif scans[i][0] == "down":
        dValue += int(scans[i][1])
    elif scans[i][0] == "up":
        dValue -= int(scans[i][1])

total = hValue*dValue
print(total)

# Part two
hValue = 0
dValue = 0
aim = 0
for i in range(len(scans)):
    if scans[i][0] == "down":
        aim += int(scans[i][1])
    elif scans[i][0] == "up":
        aim -= int(scans[i][1])
    elif scans[i][0] == "forward":
        hValue += int(scans[i][1])
        dValue += aim * int(scans[i][1])

total = hValue*dValue
print(total)


