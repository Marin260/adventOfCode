# Part one
with open('day3/input.txt') as f:
    scans = f.readlines()

scans = list(map(lambda s: s.strip(), scans))

mostComVal = [] # list for most comon values
for i in range(len(scans[0])):
    mostComVal.append([0, 0])

for num in scans:
    for index, digit in enumerate(num):
        if digit == '1':
            mostComVal[index][0] += 1
        else:
            mostComVal[index][1] +=1

# i could use ones complement to avoid using multiple variables... things for other times
gama, epsilon = '0b', '0b'
for val in mostComVal:
    if val[0] > val[1]:
        gama += '1'
        epsilon += '0'
    else: 
        gama += '0'
        epsilon += '1'


total = int(gama, 2) * int(epsilon, 2) # trnasform bin to int and mult
print(total)


# Part two
mostComVal, leastComVal = [], [] # list for most and least common values
ox, co = scans, scans
for i in range(len(scans[0])):
    listToRemoveOx = [] # elements to remove from ox list
    listToRemoveCo = [] # elements to remove from co list

    if(len(ox) != 1): 
        mostComVal.append([0, 0])
        for num in ox:
            if num[i] == '1':
                mostComVal[i][0] += 1
            else:
                mostComVal[i][1] += 1
        msbOx = '1' if mostComVal[i][0] > mostComVal[i][1] or mostComVal[i][0] == mostComVal[i][1] else '0'

        for el in ox:
            if el[i] != msbOx:
                listToRemoveOx.append(el)
        ox  = [x for x in ox if x not in listToRemoveOx] # find elements that don't match and remove them

    if(len(co) != 1): # skip if list has only one element
        leastComVal.append([0, 0])
        for num in co:
            if num[i] == '1':
                leastComVal[i][0] += 1
            else:
                leastComVal[i][1] += 1
    
        msbCo = '0' if leastComVal[i][1] < leastComVal[i][0] or leastComVal[i][0] == leastComVal[i][1] else '1'

        for el in co:
            if el[i] != msbCo:
                listToRemoveCo.append(el)
        co  = [x for x in co if x not in listToRemoveCo] # find elements that don't match and remove them


total = int('0b' + ox[0], 2) * int('0b' + co[0], 2) # trnasform bin to int and mult
print(total)




