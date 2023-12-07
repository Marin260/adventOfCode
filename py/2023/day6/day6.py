from functools import reduce


with open("input.txt", "r") as f:
    data = f.read().split("\n")

time, distance = data
time = time.split(":")[1].split()
distance = distance.split(":")[1].split()
print(time)
speed = 0

scores = []
for j, t in enumerate(time):
    margin = 0
    for i in range(int(t)):
        if i * (int(t) - i) > int(distance[j]): margin += 1
    scores.append(margin)

print(scores)
print(reduce(lambda x, y: x*y, scores))

time = "".join(time)
margin = 0

for i in range(int(time)):
    if i * (int(time) - i) > int("".join(distance)): margin += 1
print(margin)




        
