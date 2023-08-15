with open('day7/input.txt') as f:
    scans = f.readlines()

scans = [x.rstrip("\n") for x in scans]
#print(*scans, sep="\n")

def comandInInput(lineInInput: str):
    tmp = lineInInput.split()

    if lineInInput[0] == "$":
        # cd or ls
        if tmp[1] == "cd":
            return ("ENTER", tmp[2])
        else:
            return ("READ",)
    else:
        dirSize = 0
        # file size or dir
        try:
            int(tmp[0])
            return("FILE", int(tmp[0]))
        except:
            return("DIR", tmp[1])

# contruct list of directories
listOfDirectories = ["/"]
for el in scans:
    res = comandInInput(el)
    if res[0] == "DIR":
        listOfDirectories.append(res[1])


listOfDirectories = list(set(listOfDirectories))
dirSize = {}
dirVisited = {}
dirSubdirs = {}
for el in listOfDirectories:
    dirSize[el] = 0
    dirVisited[el] = 0
    dirSubdirs[el] = set()




myStack = ["/"] # current position in tree
currentDir = "/"
for el in scans:
    actionToDO = comandInInput(el)
    if actionToDO[0] == "ENTER":
        if actionToDO[1] == "..":
            myStack.pop()
        else:
            myStack.append(actionToDO[1])
        currentDir = myStack[-1]

    elif actionToDO[0] == "READ":
        dirVisited[currentDir] += 1

        #print("curently reading: {}".format(currentDir))
        pass
    elif actionToDO[0] == "FILE":
        if dirVisited[currentDir] < 2:
            dirSize[currentDir] += actionToDO[1]

    elif actionToDO[0] == "DIR":
        dirSubdirs[currentDir].add(actionToDO[1])
        pass
    pass

#for el in dirSize.items():
#    print(el)





for keys in dirSubdirs:
    dirSubdirs[keys] = list(dirSubdirs[keys])

for el in dirSubdirs.values():
    for i in range(len(el)):
        el[i] = (el[i], dirSize[el[i]])

for el in dirSubdirs.items():
    print(el)
for el in dirSize.items():
    print(el)


def recursiveSum(sumOfNeededDir: str):
    if len(dirSubdirs[sumOfNeededDir]) == 0:
        return dirSize[sumOfNeededDir]
    else:
        
        tmpDir2 = [x[0] for x in dirSubdirs[sumOfNeededDir]]
        return dirSize[sumOfNeededDir] + sum([recursiveSum(x) for x in tmpDir2])
    print(sumOfContainingDirs)
    #return dirSize[sumOfNeededDir] + recursiveSum()



