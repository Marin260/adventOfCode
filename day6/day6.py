from collections import Counter
with open('day6/input.txt') as f: # load file
    scans = f.readlines()



scans = list(map(int, scans[0].split(',')))
# transform input to dict where keys are days and values reapeating instances of that day
listOfFishDays = dict(sorted(Counter(scans).items())) 

for i in range(9): # add the keys of the days that do not exist
    try:
        listOfFishDays[i] = listOfFishDays[i]
    except KeyError:
        listOfFishDays[i] = 0
listOfFishDays = dict(sorted(listOfFishDays.items())) # no need for sorting

for i in range(256): 
    listOfFishDays['tmp'] = listOfFishDays[8] # mem of reset fish
    for k in range(9): # move all the fishies with the same day closer to 0
        if k == 0: 
            listOfFishDays[6] += listOfFishDays['tmp'] # reset the new fishies
            listOfFishDays['tmp'] = listOfFishDays[0] # newBorns
           
        if k == 8:
            listOfFishDays[k] = listOfFishDays['tmp'] # tmp value for last day
            break
        
        listOfFishDays[k] = listOfFishDays[k+1]
        

values = sum(listOfFishDays.values()) # sum all the values
print(values)