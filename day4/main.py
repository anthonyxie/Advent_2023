output = 0
cards_dict = {}
cards_amount_dict = {}
with open('input.txt') as f:
    for index, line in enumerate(f):
        total = 0
        line = line.strip()
        card, numbers = line.split(": ")
        _, card_num = card.split()
        winners, nums = numbers.split(" | ")
        for winner in winners.split(" "):
            #print(nums.split(" "))
            if winner != "" and winner in nums.split(" "):
                total += 1
        #create total num copies
        cards_amount_dict[int(card_num)] = total

        # part one:
        # if total > 0:
        #     output += 2**(total - 1)

print(cards_amount_dict)
def recurse(c_num, c_dict):
    if c_dict[c_num] == 0:
        return 1
    else: 
        return 1 + sum([recurse(c_num + offset + 1, c_dict) for offset in range(c_dict[c_num])])
for card_num in cards_amount_dict:
    output += recurse(card_num, cards_amount_dict)
print(recurse(190, cards_amount_dict))
print(output)