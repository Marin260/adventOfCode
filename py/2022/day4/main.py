with open('day4/input.txt') as f:
    scans = f.readlines()

scans = [x.rstrip("\n") for x in scans]

def createRange(el: str):
    el = el.split(",")
    el = [tuple(x.split("-")) for x in el]
    return el
def compareRange(range: list):
    el1 = range[0]
    el2 = range[1]
    cond1 = int(el1[0]) <= int(el2[0]) and int(el1[1]) >= int(el2[1])
    cond2 = int(el2[0]) <= int(el1[0]) and int(el2[1]) >= int(el1[1])
    if cond1 or cond2:
        return 1
    else:
        return 0

scans = [createRange(x) for x in scans]
tot = 0
for el in scans:
    tot += compareRange(el)
print(tot)

def partTwoOverlap(lt:list):    
    if int(lt[0][1]) == int(lt[1][0]) or int(lt[0][0]) == int(lt[1][1]):
        totSum += 1
    elif int(lt[0][1]) == int(lt[1][1]) or int(lt[0][0]) == int(lt[1][0]):
        totSum += 1
    elif int(lt[0][0]) <= int(lt[1][0]) <= int(lt[0][1]):
        totSum += 1
    elif int(lt[0][0]) <= int(lt[1][1]) <= int(lt[0][1]):
        totSum += 1
    elif int(lt[1][0]) <= int(lt[0][0]) <= int(lt[1][1]):
        totSum += 1
    elif int(lt[1][0]) <= int(lt[0][1]) <= int(lt[1][1]):
        totSum += 1
    return totSum


tot2 = 0
tot3 = 0
for el in scans:
    tot2 += partTwoOverlap(el)
print(tot2)
