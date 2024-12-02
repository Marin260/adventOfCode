with open("input.txt", 'r') as f:
    data = f.read().split("\n")
    data = [[int(y) for y in x.split()] for x in data]


def validList(line):
    diff_is_ok = True
    inc_or_dec = (sorted(line) == line or sorted(line, reverse=True) == line)
    for i in range(len(line)-1):
        if abs(line[i] - line[i+1]) not in (1, 2, 3):
            diff_is_ok = False 
    if diff_is_ok == True and inc_or_dec:
        return True
    return False


tot1 = 0
tot2 = 0
for line in data:
    valid_with_tolerance = False
    if validList(line):
        tot1 += 1

    for i in range(len(line)):
        if validList(line[:i] + line[i+1:]):
            valid_with_tolerance = True

    if valid_with_tolerance:
        tot2 += 1

print(tot1)
print(tot2)
