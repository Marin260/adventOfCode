with open('day7/input.txt') as f: # load file
    scans = f.readlines()

scans = list(map(int, scans[0].split(','))) # parse
min_fuel = 1000000000000
for i in range(len(scans)):
    tmp = sum([(abs(sub - i)*(abs(sub - i)+1))/2 for sub in scans]) 
    if tmp < min_fuel:
        min_fuel = tmp

print(min_fuel)