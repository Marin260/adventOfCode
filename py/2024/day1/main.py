with open('input.txt', 'r') as f:
    data = f.read().split("\n")

data = [x.split() for x in data]
l = [int(x[0]) for x in data]
r = [int(x[1]) for x in data]

l.sort()
r.sort()

tot = 0
tot2 = 0 
for i in range(len(l)):
    tot += abs(l[i] - r[i])
    tot2 += l[i] * r.count(l[i])
    print(l[i], " -> ", l[i], " * ", r.count(l[i]))

print(tot)
print(tot2)
