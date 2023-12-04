from collections import defaultdict

with open("input.txt", "r") as f:
    data = f.read().split("\n")

data = [line.split(":")[1] for line in data]

def po(data):
    tot, tot2 = 0, 0
    scratchers = defaultdict(lambda: int()+1)

    for i, card in enumerate(data):
        s, winning = card.split("| ")
        s = s.split()
        winning = winning.split()
        points = set(s).intersection(winning)

        for score in range(1, len(points)+1):
            for _ in range(scratchers.get(i, 1)):
                scratchers[i+score] += 1
        if len(points):
            tot += 2**(len(points)-1)
        tot2 += scratchers.get(i, 1)
        
    print(tot)
    print(tot2)

po(data)
