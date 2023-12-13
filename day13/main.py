import functools
from itertools import combinations, pairwise, permutations
def printy(grid):
    for l in grid:
        print(l)

input = []
ing = []
current = []
def find_reflect(input):    
    for i in range(1, len(input)):
        above = input[0:i]
        below = input[i:]
        min_len = min(len(above), len(below))
        if above[-1 * min_len:] == below[0:min_len][::-1]:
            return i
    return -1
        
with open('input.txt') as f:
    for index, line in enumerate(f):
        line = line.strip()
        input.append(line)
        if len(line) > 0:
            current.append(line)
        if len(line) <= 1:
            ing.append(current)
            current = []
ing.append(current)
num_rows = 0
num_cols = 0

# printy(ing[-1])
# printy(ing[-2])
# for j, input in enumerate(ing):
#     input_trans = []
#     for index, line in enumerate(input[0]):
#         col = [sub[index] for sub in input]
#         input_trans.append(''.join(col[::-1]))
    
#     if find_reflect(input) != -1:
#         num_rows += find_reflect(input)
#     if find_reflect(input_trans) != -1:
#         num_cols += find_reflect(input_trans)

# print(num_cols + 100 * num_rows)
def find_reflect_2(input): 
    out = []   
    for i in range(1, len(input)):
        above = input[0:i]
        below = input[i:]
        min_len = min(len(above), len(below))
        if above[-1 * min_len:] == below[0:min_len][::-1]:
            out.append(i)
    if len(out) == 0:
        return -1
    else:
        return(out)
num_cols = 0
num_rows = 0
for j, input in enumerate(ing):
    input_trans = []
    for index, line in enumerate(input[0]):
        col = [sub[index] for sub in input]
        input_trans.append(''.join(col[::-1]))

    #printy(input_trans)

    flag = False
    for y in range(len(input)):
        for x in range(len(input[0])):
            new_input = input[::1]
            assert(len(new_input) == len(input))
            if x < len(input[0]) - 1:
                new_input[y] = input[y][0:x] + str("#" if input[y][x] == "." else ".") + input[y][x+1:]
            else:
                new_input[y] = input[y][0:x] + str("#" if input[y][x] == "." else ".")
            if j == 89 and y == len(input) - 1 and x == 5:
                printy(new_input)
                print(find_reflect(new_input))
                print(find_reflect)
                print("")
            assert(len(new_input[y]) == len(input[y]))
            if find_reflect_2(new_input) != -1:
                for new_reflection in find_reflect_2(new_input):
                    if new_reflection != find_reflect(input):
                        if not flag:
                            num_rows += new_reflection
                            print("indie", j)
                            flag = True
                

    input = input_trans
    flag = False
    for y in range(len(input)):
        for x in range(len(input[0])):
            new_input = input[::1]
            assert(len(new_input) == len(input))
            if x < len(input[0]) - 1:
                new_input[y] = input[y][0:x] + str("#" if input[y][x] == "." else ".") + input[y][x+1:]
            else:
                new_input[y] = input[y][0:x] + str("#" if input[y][x] == "." else ".")
            if j == 89 and y == len(input) - 1 and x == 5:
                printy(new_input)
                print(find_reflect(new_input))
                print(find_reflect)
                print("")
            assert(len(new_input[y]) == len(input[y]))
            if find_reflect_2(new_input) != -1:
                for new_reflection in find_reflect_2(new_input):
                    if new_reflection != find_reflect(input):
                        if not flag:
                            num_cols += new_reflection
                            print("indie", j)
                            flag = True

print(num_cols + 100 * num_rows)