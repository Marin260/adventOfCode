with open('day2/input.txt') as f:
    scans = f.readlines()

scans = [x.rstrip("\n").split() for x in scans]

crypt = {
    "X" : "A",
    "Y" : "B",
    "Z" : "C",
    "A" : 1,
    "B" : 2,
    "C" : 3,
}
crypt2 = {
    "X" :  0,
    "Y" :  3,
    "Z" :  6,
    "A" : 1,
    "B" : 2,
    "C" : 3,
}


score2 = 0
for i in range(len(scans)):
    if scans[i][0] == "A": # rock
        if crypt2[scans[i][1]] == 0: # sci 3
            score2 += 3 + 0
        elif crypt2[scans[i][1]] == 6: # pap 2
            score2 += 2 + 6
    elif scans[i][0] == "B": # pap
        if crypt2[scans[i][1]] == 0: # rock 1
            score2 += 1 + 0
        elif crypt2[scans[i][1]] == 6:
            score2 += 3 + 6
    elif scans[i][0] == "C":
        if crypt2[scans[i][1]] == 0:
            score2 += 2 + 0
        elif crypt2[scans[i][1]] == 6:
            score2 += 1 + 6
    if scans[i][1] == "Y":
        score2 += 3 + crypt2[scans[i][0]]

score = 0
for i in range(len(scans)):
    scans[i][1] = crypt[scans[i][1]]
    if scans[i][0] == scans[i][1]:
        score += 3 + crypt[scans[i][1]]
    elif ord(scans[i][0]) - ord(scans[i][1]) in (-1, 2):
        score += 6 + crypt[scans[i][1]]
    elif ord(scans[i][0]) - ord(scans[i][1]) in (1, -2):
        score += 0 + crypt[scans[i][1]]
    

print(score)
print(score2)


        

