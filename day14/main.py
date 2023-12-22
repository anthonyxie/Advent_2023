import functools
from itertools import combinations, pairwise, permutations
def printy(grid):
    for l in grid:
        print(l)

input = []
        
with open('input.txt') as f:
    for index, line in enumerate(f):
        line = line.strip()
        input.append([c for c in line])



def pushballs(input):
    fixed = [[False if i != "#" else True for i in row] for row in input]
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == "O":
                curr = i
                while curr > 0:
                    if fixed[curr - 1][j] == True:
                        break    
                    curr -= 1
                input[i][j] = "."
                input[curr][j] = "O"
                fixed[curr][j] = True
    return input

def trans_one(matrix):
    output = [[mat[i] for mat in matrix] for i in range(len(matrix[0]))]
    return output
def trans_two(matrix):
    output = [[mat[i] for mat in matrix][::-1] for i in range(len(matrix[0]))[::-1]]
    return output
def upside_down(input):
    output = [row for row in input[::-1]]
    return output
def rd(input):
    output = [row for row in input[::-1]]
    return output


# printy(input)
# print("")
# printy(pushballs(trans_two(input)))
# print("")
# printy(trans_two(pushballs(trans_two(input))))
# print("")
# printy(pushballs(trans_one(input)))
# print("")
# printy(trans_one(pushballs(trans_one(input))))
output = 0




d = {}
for x in range(1000):
    input = pushballs(input)
    input = trans_one(pushballs(trans_one(input)))
    input = rd(pushballs(rd(input)))
    input = trans_two(pushballs(trans_two(input)))
    output = 0 
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == "O":
                output += len(input) - i
    #print(output)
    if output not in d:
        d[output] = [x]
    elif len(d[output]) == 1:
        d[output].append(x)
for t in [thing for thing in d.keys() if len(d[thing]) > 1]:
    one, two = d[t]
    if (1000000000 - 1 - one) % (two - one) == 0:
        print(d)
        print(t)
        
#printy(input)


# for i in range(len(input)):
#     for j in range(len(input[0])):
#         if input[i][j] == "O":
#             output += len(input) - i
# #printy(input)
# print(output)

        