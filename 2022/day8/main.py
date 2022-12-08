with open('input.txt') as f:
    scans = f.readlines()

scans = [x.rstrip("\n") for x in scans]
scans = [[int(y) for y in x] for x in scans]

outerBorder = len(scans) * 4 - 4

def check_left(tree, row, col):
    x = 0
    for i in range(len(scans)):
        if i == col:
            x = 1
            break
        if tree <= scans[row][i]: break
    return x

def check_top(tree, row, col):
    x = 0
    for i in range(len(scans)):
        if i == row:
            x = 1
            break
        if tree <= scans[i][col]: break
    return x

def check_right(tree, row, col):
    for i in range(col+1, len(scans)):
        if tree <= scans[row][i]: return 0
    return 1

def check_bot(tree, row, col):
    for i in range(row+1, len(scans)):
        if tree <= scans[i][col]: return 0
    return 1
            
def sum_left(tree, row, col):
    visible_trees = 0
    for i in range(col-1, -1, -1):
        # check left
        if tree >= scans[row][i]: visible_trees += 1
        if tree <= scans[row][i]:
            if tree < scans[row][i]: visible_trees += 1
            break
    return visible_trees

def sum_top(tree, row, col):
    visible_trees = 0
    for i in range(row-1, -1, -1):
        if tree >= scans[i][col]: visible_trees += 1
        if tree <= scans[i][col]:
            if tree < scans[i][col]: visible_trees += 1
            break
    return visible_trees

def sum_right(tree, row, col):
    visible_trees = 0
    for i in range(col+1, len(scans), +1):
        if tree >= scans[row][i]: visible_trees += 1
        if tree <= scans[row][i]:
            if tree < scans[row][i]: visible_trees += 1
            break
    return visible_trees

def sum_down(tree, row, col):
    visible_trees = 0
    for i in range(row+1, len(scans), +1):
        if tree >= scans[i][col]: visible_trees += 1
        if tree <= scans[i][col]:
            if tree < scans[i][col]:visible_trees += 1
            break
    return visible_trees

scanicV = []
for i in range(1, len(scans[1:])):
    for j in range(1, len(scans[i][1:])):
        x = check_top(scans[i][j], i, j) + check_left(scans[i][j], i, j) + check_bot(scans[i][j], i, j) + check_right(scans[i][j], i, j)
        y = sum_left(scans[i][j], i, j) * sum_top(scans[i][j], i, j) * sum_right(scans[i][j], i, j) * sum_down(scans[i][j], i, j)
        scanicV.append(y)
        if x > 0: outerBorder += 1

print(outerBorder)
print(max(scanicV))