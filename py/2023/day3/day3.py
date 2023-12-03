

from collections import defaultdict
from functools import reduce

with open("input.txt", "r") as f:
    data = f.read().split("\n")

data = [[char for char in line] for line in data]
data = [["."]+line+["."] for line in data]
e = len(data[0]) * ["."]
data.append(e)
data.insert(0, e)

def po(data):
    tot1, tot2 = 0, 0
    num = ""
    gears = defaultdict(list)
    
    for i, row in enumerate(data):
        countIn = False
        isGear = False
        for j, char in enumerate(row):
            if char.isdigit():
                for k in [-1, 0, 1]:
                    for l in [-1, 0, 1]:
                        if data[i+k][j+l] != "." and not data[i+k][j+l].isdigit():
                            countIn = True
                        if data[i+k][j+l] == "*":
                            isGear = (i+k, j+l)
                num += char
            elif not char.isdigit():
                if isGear:
                    gears[isGear].append(int(num))
                    isGear = False
                if countIn and len(num) > 0:
                    tot1 += int(num)
                    num = ""
                    countIn = False
                else:
                    num = ""
    for coordinate in gears.keys():
        if len(gears[coordinate]) > 1:
            tot2 += reduce(lambda x, y: x*y, gears[coordinate])
        
    print(tot1)
    print(tot2)
po(data)

                