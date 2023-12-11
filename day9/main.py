
sequences = []
with open('input.txt') as f:
    for index, line in enumerate(f):
        line = line.strip()
        sequences.append([int(i) for i in line.split(" ")])

output = 0
def checkAllTrue(list):
    list = [i == 0 for i in list]
    if list == []:
        return True
    for i in list:
        if i is False:
            return True
    return False

for sequence in sequences:
    s_copy = sequence
    curr = []
    diffs = []
    print(sequence)
    last = sequence[0]
    currs = []
    while checkAllTrue(curr):
        curr = []
        for i, num in enumerate(sequence):
            if i > 0:
                curr.append(sequence[i] - sequence[i - 1])
        sequence = curr
        currs.append(curr)
    
    diff = 0
    print(currs)
    for curr in reversed(currs[:len(currs) - 1]):
        diff = curr[0] - diff
    output += last - diff
    print(last + diff)
print(output)


        
