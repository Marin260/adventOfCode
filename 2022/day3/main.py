with open('day3/input.txt') as f:
    scans = f.readlines()

scans = [x.rstrip("\n") for x in scans]

#print(scans)
def returnPriority(x):
    el = set(x[0:int(len(x)/2)]) & set(x[int(len(x)/2):])
    el = str(list(el)[0])
    if el.isupper():
        return ord(el) - ord("A") + 27
    else:
        return ord(el) - ord("a") + 1



scansSet = [returnPriority(x) for x in scans]
scansSet = sum(scansSet)
print(scansSet)

partTwoSet = []
for i in range(0, len(scans), 3):
    partTwoSet.append(set(scans[i]) & set(scans[i+1]) & set(scans[i+2]))

def returnPriorityPartTwo(el):
    el = str(list(el)[0])
    if el.isupper():
        return ord(el) - ord("A") + 27
    else:
        return ord(el) - ord("a") + 1

partTwoSet = [returnPriorityPartTwo(x) for x in partTwoSet]
print(sum(partTwoSet))

