with open('day6/input.txt') as f:
    scans = f.readlines()[0].rstrip("\n")

for i in range(len(scans[:-13])): # part one change 13 -> to 3 
    if len(set(scans[i:i+14])) > 13: # part one change 13 -> 3 and 14 -> 4
        print(i+14) # part one change 14 -> 4
        break

