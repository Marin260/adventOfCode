with open('input.txt') as f:
    scans = f.readlines()

scans = [x.rstrip("\n") for x in scans]

def comandInInput(lineInInput: str):
    tmp = lineInInput.split()

    if lineInInput[0] == "$":
        # cd or ls
        if tmp[1] == "cd":
            return ("ENTER", tmp[2])
        else:
            return ("READ",)
    else:
        try:
            int(tmp[0])
            return("FILE", int(tmp[0]))
        except:
            return("DIR", tmp[1])


listOfComands = [comandInInput(x) for x in scans]

history = ["/"]
dictPaths = {"/":0}
path="/" # I am in this directory

for comand in listOfComands[1:]:
    if comand[0] == "ENTER":
        if comand[1] == "..":
            path = path[:-(len(history[-1])+1)]
            history.pop()
        else:
            path = path + comand[1] + "/"
            history.append(comand[1])
            if dictPaths.get(path, 0) == 0:
                dictPaths[path] = 0
        
    elif comand[0] == "FILE":
        dictPaths[path] += comand[1]


def sumSizeOfDir(inputPath: str):
    x = sum([dictPaths[absPath] for absPath in dictPaths.keys() if checkIfSubPath(inputPath, absPath)])
    return x

def checkIfSubPath(superiorPath: str, inferiorPath:str):
    if len(superiorPath) > len(inferiorPath):
        return False
    for i in range(len(superiorPath)):
        if superiorPath[i] != inferiorPath[i]:
            return False
    return True


x = [sumSizeOfDir(el) for el in dictPaths.keys() if sumSizeOfDir(el) < 100_000]
print(sum(x))


avab = 70_000_000 - sumSizeOfDir("/")
newx = [sumSizeOfDir(el) for el in dictPaths.keys()]
newx.sort()
tmp = min([el for el in newx if avab + el > 30_000_000])
print(tmp)