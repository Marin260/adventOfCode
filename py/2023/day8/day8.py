import time


with open("input.txt", "r") as f:
    data = f.read().split("\n")

def endInZ(d: dict):
    x = True
    z = 0
    for val in d.values():
        if val[-1] != "Z": x = False
        if val[-1] == "Z": z += 1
    if z > 2:
        print("total of Z:", z)
    return x


nodes = {}
for line in data[2:]:
    parent, children = line.split(" = ")
    children = children.lstrip("(").rstrip(")").split(", ")
    nodes[parent] = children

i = 0
steps = 0
steps2 = 0
curent_node = "AAA"



while i < len(data[0]):
    path = data[0][i]

    if path == "L": curent_node = nodes[curent_node][0]
    else: curent_node = nodes[curent_node][1]
    steps += 1
    
    if curent_node == "ZZZ": 
        break

    if i == (len(data[0])-1): i = 0
    else: i+=1
print(steps)


# theoratically this thing works for part to but there is no way for it to finish
# should te cycle from A to Z for each element and then sync them up
i = 0
e = {}
startNodes = filter(lambda x: x[-1] == "A", nodes.keys())
startNodes = list(startNodes)
while i < len(data[0]):
    path = data[0][i]
    for el in startNodes:
        if path == "L":
            e[el] = nodes[el][0]
        else: 
            e[el] = nodes[el][1]
    steps2 += 1
    if endInZ(e): break
    startNodes = list(e.values())
    e = {}


    if i == (len(data[0])-1): i = 0
    else: i+=1
print(steps2)
