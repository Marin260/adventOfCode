with open('day1/input.txt') as f:
    scans = f.readlines()


scans = [int(x.rstrip("\n")) if x.rstrip("\n")!="" else "" for x in scans]

def checkIfBiggerThanOneInList(myList: list, el: int):
    if el > min(myList):
        myList[myList.index(min(myList))] = el
    return myList

maxi = 0
suma = 0
top = [0, 0 ,0]
for el in scans:
    if el != "":
        suma += el
    else:
        if suma > maxi:
            maxi = suma
        top = checkIfBiggerThanOneInList(top, suma)
        suma = 0
print(maxi)
print(sum(top))