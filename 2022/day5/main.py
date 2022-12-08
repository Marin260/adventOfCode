with open('day5/input.txt') as f:
    scans = f.readlines()

scans = [x.rstrip("\n") for x in scans[10:]]

initStack = {
    "1" : ["T", "D", "W", "Z", "W", "P"],
    "2" : ["L", "S", "W", "V", "F", "J", "D"],
    "3" : ["Z", "M", "L", "S", "V", "T", "B", "H"],
    "4" : ["R", "S", "J"],
    "5" : ["C", "Z", "B", "G", "F", "M", "L", "W"],
    "6" : ["Q", "W", "V", "H", "Z", "R", "G", "B"],
    "7" : ["V", "J", "P", "C", "B", "D", "N"],
    "8" : ["P", "T", "B", "Q"],
    "9" : ["H", "G", "Z", "R", "C"]
}
for i in range(len(scans)):
    scans[i] = [el for el in scans[i].split() if el.isdigit()]

def moveCrate(listToRemove: list, listToAdd: list):
    listToAdd.append(listToRemove[-1])
    listToRemove.pop()
for el in scans:
    for i in range(int(el[0])):
        moveCrate(initStack[el[1]], initStack[el[2]])

ans = ""
for el in initStack.values():
    ans+=el[-1]
print(ans)

initStack2 = {
    "1" : ["T", "D", "W", "Z", "W", "P"],
    "2" : ["L", "S", "W", "V", "F", "J", "D"],
    "3" : ["Z", "M", "L", "S", "V", "T", "B", "H"],
    "4" : ["R", "S", "J"],
    "5" : ["C", "Z", "B", "G", "F", "M", "L", "W"],
    "6" : ["Q", "W", "V", "H", "Z", "R", "G", "B"],
    "7" : ["V", "J", "P", "C", "B", "D", "N"],
    "8" : ["P", "T", "B", "Q"],
    "9" : ["H", "G", "Z", "R", "C"]
}

def moveCrate2(listToRemove: list, listToAdd: list, numOfEls: int):
    tmp = listToRemove[-numOfEls:]
    listToAdd = listToAdd + tmp
    listToRemove = listToRemove[0:-numOfEls]
    return (listToRemove, listToAdd)

for i in range(len(scans)):
    x = moveCrate2(initStack2[scans[i][1]], initStack2[scans[i][2]], int(scans[i][0]))
    initStack2[scans[i][1]], initStack2[scans[i][2]] = x[0], x[1]
print(scans[0])
moveCrate2(initStack2[scans[0][1]], initStack2[scans[0][2]], int(scans[0][0]))
print()
for el in initStack2.items():
    print(el)
ans2 = ""
for el in initStack2.values():
    ans2+=el[-1]
print(ans2)