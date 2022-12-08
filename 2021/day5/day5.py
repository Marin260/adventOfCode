# Part one
import numpy as np
import operator
with open('day5/input.txt') as f: # load file
    scans = f.readlines()

def maxInScans(setOfScans): # find bigest number in a set
    maxValues = []
    for scan in setOfScans: # go through a 2d array
        for tp in scan:
            maxValues.append(max(tp))
    return max(maxValues) # return bigest value

for i in range(len(scans)): # parse the input
    scans[i] = scans[i].rstrip('\n') # remove \n
    scans[i] = scans[i].split(' -> ') # divide the string on ->, result 2 arrays(string)
    for j in range(len(scans[i])):
        scans[i][j] = tuple(map(int, scans[i][j].split(','))) # split and convert the values to int, put the result into a tuple

size = (maxInScans(scans)+1, maxInScans(scans)+1) # create the size of the field
plot = np.zeros(size, dtype=int).tolist() # create 2d field with 0, convert ndarray to list
for scan in scans: # go through input
    y, x = scan[0][1], scan[0][0] # first tuple of two, tarting points
    travelY = scan[0][1] - scan[1][1] # find the distance from y1 to y2
    travelX = scan[0][0] - scan[1][0] # find the distance from x1 to x2
    opX = operator.add if travelX < 0 else operator.sub # if the travel is negative then we go forward else backwards
    opY = operator.add if travelY < 0 else operator.sub
    if scan[0][0] == scan[1][0]: # vertical lines
        fixPos = scan[0][0]
        for i in range(abs(travelY)+1):
            plot[opY(y, i)][fixPos] += 1
    elif scan[0][1] == scan[1][1]: # horizontal lines
        fixPos = scan[0][1]
        for i in range(abs(travelX)+1):
            plot[fixPos][opX(x, i)] += 1
    else: # diagonals
        for i in range(abs(travelX)+1):
            plot[opY(y, i)][opX(x, i)] += 1

numOfIntersections = 0
for row in plot: # go through the 2d array and count values bigger than 1
    for num in row:
        if num > 1:
            numOfIntersections += 1
print(numOfIntersections)