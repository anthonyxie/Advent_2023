import functools
from itertools import combinations, pairwise, permutations
def printy(grid):
    for l in grid:
        print(l)

input = []
i = []
with open('input.txt') as f:
    for index, line in enumerate(f):
        line = line.strip()
        input.append(line)
        path, combos = line.split()
        combos = combos.split(",")
        i.append((path, tuple(combos)))


    
# @functools.cache
# def calculateplacements(path, combos):
#     print("path:")
#     print(path)
#     print("combos:", combos)
#     if len(combos) == 0:
#         return 0 if '#' in path else 1
        
    
#     for index, combo in enumerate(combos):
#         combo = int(combo)
#         if path.find("#") != -1:
#             subpath = path[0:min(path.find("#") + 1, len(path))]
#         else:
#             subpath = path
#         #print(combos)
#         if combo > len(path):
#             return 0
#         total = 0  
#         for i, c in enumerate(subpath):
#             if all(ch in "#?" for ch in path[i:i+combo]):
#                 if i + combo >= len(path) or path[i + combo] in "?.": #bang bang its poggers
#                     new_path = path[i + combo + 1:]
#                     total += calculateplacements(new_path, tuple(list(combos[0:index] + combos[index + 1:])))
#         return total

@functools.cache
def calculateplacements(path, combos):
    #print("path:")
    #print(path)
    #print("combos:", combos)
    if len(combos) == 0:
        return 0 if '#' in path else 1
        
    combo, *rest = combos

    combo = int(combo)
    if path.find("#") != -1:
        subpath = path[0:min(path.find("#") + 1, len(path))]
    else:
        subpath = path
    #print(combos)
    if combo > len(path):
        return 0
    total = 0  
    for i, c in enumerate(subpath):
        if all(ch in "#?" for ch in path[i:i+combo]):
            if i + combo == len(path) or (i + combo < len(path) and path[i + combo] in "?."): 
                #bang bang its poggers
                    new_path = path[i + combo + 1:]
                    total += calculateplacements(new_path, tuple(rest))
    return total

output = 0   
for path, combos in i:
    path = '?'.join(path for i in range(5))
    combos = combos * 5
    print(path, combos)
    output += calculateplacements(path, combos)
    print(calculateplacements(path, combos))
print(output)
        
            

    

