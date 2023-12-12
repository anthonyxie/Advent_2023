from itertools import combinations, pairwise, permutations
def printy(grid):
    for l in grid:
        print(l)

input = []
with open('input.txt') as f:
    for index, line in enumerate(f):
        line = line.strip()
        input.append(line)
input_trans = []
for index, line in enumerate(input[0]):
    input_trans.append(''.join([sub[index] for sub in input]))
printy(input)
print("doggis")
printy(input_trans)
rows = []
cols = []
for index, l in enumerate(input):
    flag = False
    for c in l:
        if c != ".":
            flag = True
    if flag == False:
        rows.append(index)


printy(input)
print("")
for index, l in enumerate(input_trans):
    flag = False
    for c in l:
        if c != ".":
            flag = True
    if flag == False:
        cols.append(index)
# print(rows)
# print(cols)
# i = 0
# for row_num in rows:
#     input.insert(row_num + i, ''.join(["." for i in input[0]]))
#     i += 1
# printy(input)
# for index, row in enumerate(input):
#     i = 0
#     for col_num in cols:
#         input[index] = input[index][0:col_num + i] + "." + input[index][col_num + i:]
#         i += 1
# printy(input)
points = []
for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == "#":
            points.append((x, y))

output = 0
seen = []
dists = []
for p1, p2 in combinations(points, 2):
    minx, maxx = min(p2[0], p1[0]), max(p2[0], p1[0])
    miny, maxy = min(p2[1], p1[1]), max(p2[1], p1[1])
    dist_x = 0
    dist_y = 0
    for j in range(minx, maxx):
        if j in cols:
            dist_x += 999999
            #dist_x += 1
        dist_x += 1
    for i in range(miny, maxy):
        if i in rows:
            dist_y += 999999
            #dist_y += 1
        dist_y += 1
    dist = dist_x + dist_y
    dists.append(dist)
    output += dist
print(output)