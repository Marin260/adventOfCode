import math

with open("input.txt", "r") as f:
    data = f.read().split("\n")

nodes = {}
for line in data[2:]:
    parent, children = line.split(" = ")
    children = children.lstrip("(").rstrip(")").split(", ")
    nodes[parent] = children

# part one
steps, i = 0, 0
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

# part two
def findFirstZ(el, data):
    steps, i = 0, 0
    while i < len(data[0]):
        path = data[0][i]

        if el[-1] == "Z": break

        if path == "L": el = nodes[el][0]
        else:  el = nodes[el][1]
        steps += 1

        if i == (len(data[0])-1): i = 0
        else: i += 1

    return steps


startNodes = filter(lambda x: x[-1] == "A", nodes.keys())

minCycles = [] 
for node in startNodes:
    minCycles.append(findFirstZ(node, data))

print(math.lcm(*minCycles))
