from itertools import groupby


with open("input.txt", "r") as f:
    data = f.read().split("\n")

data = [line.split() for line in data]

data2 = []
data3 = []

def cardOccur(hand, joker=False):
    occ = []
    jokers = 0
    for card in set(hand):
        if joker:
            if card == "J":
                jokers += hand.count(card)
            else:
                occ.append(hand.count(card))
        else:
            occ.append(hand.count(card))
    occ.sort(reverse=True)
    if joker:
        if len(occ) > 0:
            occ[0] += jokers
        else:
            occ = [jokers]    
    return occ

def rankHand(hand, joker=False):
    hand = hand.replace("T", "V")
    hand = hand.replace("J", "W")
    hand = hand.replace("Q", "X")
    hand = hand.replace("K", "Y")
    hand = hand.replace("A", "Z")
    if joker:
        hand = hand.replace("W", "1")
    return hand

def calcScenario(occ):
    match occ:
        case [5]: return 6
        case [4, 1]: return 5
        case [3, 2]: return 4
        case [3, 1, 1]: return 3
        case [2, 2, 1]: return 2
        case [2, 1, 1, 1]: return 1
        case [1, 1, 1, 1, 1]: return 0

for line in data:
    card, score = line

    card1 = rankHand(card)
    card2 = rankHand(card, True)

    tmpLine1 = [card1, score]
    tmpLine1.append(calcScenario(cardOccur(line[0])))

    tmpLine2 = [card2, score]
    tmpLine2.append(calcScenario(cardOccur(line[0], True)))

    data2.append(tmpLine1)
    data3.append(tmpLine2)

data2 = sorted(data2, key=lambda e: (-e[2], -ord(e[0][0]), -ord(e[0][1]), -ord(e[0][2]), -ord(e[0][3]), -ord(e[0][4])))
data3 = sorted(data3, key=lambda e: (-e[2], -ord(e[0][0]), -ord(e[0][1]), -ord(e[0][2]), -ord(e[0][3]), -ord(e[0][4])))

tot1, tot2 = 0, 0
for i, line in enumerate(reversed(data2)):
    tot1 += (i+1) * int(line[1])

for i, line in enumerate(reversed(data3)):
    tot2 += (i+1) * int(line[1])


print(tot1)
print(tot2)

