from collections import Counter
import functools
def rank(hand):
    counts = Counter(hand)
    if len(counts) == 1:
        return 0
    if len(counts) == 2:
        if max(counts.values()) == 4:
            return 1
        return 2

    if max(counts.values()) == 3:
        return 3

    if sum(v == 2 for v in counts.values()) == 2:
        return 4

    if len(counts) < 5:
        return 5

    return 6

def maxrank(hand):
    counts = Counter(c for c in hand)
    if 'J' not in counts:
        return rank(hand)
    js = counts.pop('J')

    if not counts:
        return 0
    max_char = max(counts, key=counts.get)
    all_chars = []
    for k, v in counts.items():
        all_chars.extend(k for _ in range(v))

    all_chars.extend(max_char for _ in range(js))
    return rank(''.join(all_chars))


#ranks = { k : i for i, k in enumerate(reversed('23456789TJQKA')) }
ranks = { k : i for i, k in enumerate(reversed('J23456789TQKA')) }
def cmp_hand(hand1, hand2):
    hand1, hand2 = hand1[0], hand2[0]
    if maxrank(hand1) != maxrank(hand2):
        return maxrank(hand2) - maxrank(hand1)
    else:
        for i in range(len(hand1)):
            if ranks[hand1[i]] != ranks[hand2[i]]:
                return ranks[hand2[i]] - ranks[hand1[i]]


lines = []
hands = []
with open('input.txt') as f:
    for index, line in enumerate(f):
        lines.append(line.strip())
print(lines)
for line in lines:
    hand, bid = line.split(" ")
    hands.append((hand, bid))



hands = sorted(hands, key=functools.cmp_to_key(cmp_hand))
print(list(reversed(hands)))
print(len(hands))
output = 0
for i, hand in enumerate(hands):
    # print(i + 1, hand[0], hand[1])
    # print((i + 1) * int(hand[1]))
    output += (i + 1) * int(hand[1])

print(output)
