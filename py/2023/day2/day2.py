from functools import reduce

with open("input.txt", "r") as f:
    data = f.read().split("\n")

limits = {"red": 12, "green": 13, "blue": 14}

def po(data):
    partOne, partTwo = 0, 0

    for line in data:
        possible = True
        gid, games  = line.lstrip("Game ").split(":")
        games = games.replace(";", ",")[1:].split(", ")
        minTotal = {"red": 1, "green": 1, "blue": 1}

        for game in games:
            val, color = game.split()
            if int(val) > minTotal[color]: minTotal[color] = int(val)
            if int(val) > limits[color]: possible = False

        if possible: partOne += int(gid)
        partTwo += reduce(lambda x, y: x*y, minTotal.values())

    print(partOne)
    print(partTwo)

po(data)
