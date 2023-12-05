from collections import defaultdict

with open("input2.txt", "r") as f:
    data = f.read()

data = data.split("\n\n")
seeds = list(map(int, data[0].split(":")[1].split()))
data = data[1:]
data = [[list(map(int, x.split())) for x in line.split("\n")[1:]] for line in data]

def isInRange(source, step, seed):
    if seed >= source and seed < (source + step):
        return True
    else:
        False

def calcMap(dest, source, seed):
    mapDiff = seed - source
    return dest + mapDiff

def po(data, seeds):
    minLoc = 1000000000000000
    for seed in seeds:
        mapedSeed = seed
        for line in data:
            print(line)
            for mp in line:
                if isInRange(mp[1], mp[2], mapedSeed):
                    mapedSeed = calcMap(mp[0], mp[1], mapedSeed)
                    break
        if mapedSeed < minLoc: minLoc = mapedSeed
    print(minLoc)

po(data, seeds)

# not solution for part two yet
# this thing blows up if i use the same function
# have to find another way with intervals