# Part one
with open('input.txt') as f:
    scans = f.readlines()

num_of_depth_changes = 0
scans[0] = int(scans[0].rstrip("\n")) # first skiped value

for i in range(len(scans[1:])): # go through the list
    scans[i+1] = int(scans[i+1].rstrip("\n")) # remve \n and trnsform to int
    if scans[i+1] > scans[i]: # if the number b4 was bigger add 1 to cout
        num_of_depth_changes +=1


print(num_of_depth_changes)   
# Part two

num_of_depth_changes = 0
tmpSum = scans[0] + scans[1] + scans[2]

for i in range(len(scans[1:-2])): # go through the list
    curSum = scans[i+1] + scans[i+2] + scans[i+3] # sum 3 consecutive elements
    if curSum > tmpSum: # if the sum b4 was bigger add 1 to cout
        num_of_depth_changes +=1
    tmpSum = curSum
print(num_of_depth_changes)

