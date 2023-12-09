with open("input.txt", "r") as f:
    data = f.read().split("\n")

data = [list(map(int, line.split())) for line in data]

def calcNextSequence(sequence: list)->list:
    tmp = []
    for i in range(len(sequence)-1):
        tmp.append(sequence[i+1] - sequence[i])
    return tmp

def checkIfZeros(sequence: list)->bool:
    return  all(num==0 for num in sequence)

def calcSequence(sequence: list) -> int:
    history = [sequence[-1]]
    s = sequence
    while not checkIfZeros(s):
        s = calcNextSequence(s)
        history.append(s[-1])
    return sum(history)

def calcSequenceBack(sequence:list) -> int:
    history = [sequence[0]]
    s = sequence
    while not checkIfZeros(s):
        s = calcNextSequence(s)
        history.insert(0, s[0])

    st = history[0]
    for x in range(1, len(history)):
        st = history[x] - st
    return st


po, pt = 0, 0
for line in data:
    po += calcSequence(line)
    pt += calcSequenceBack(line)

print(po)
print(pt)
