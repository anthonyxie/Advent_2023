from collections import deque


sequences = []
input = []
with open('input.txt') as f:
    for index, line in enumerate(f):
        line = line.strip()
        input.append(line)
        #sequences.append([int(i) for i in line.split(" ")])

startx, starty = 0, 0
for i, l in enumerate(input):
    if "S" in l:
        startx, starty =  l.find("S"), i
seen = []

max_x = 0
max_y = 0
steps = 0
hehe = []
testgrid = [[-1 for i in range(len(input[0]))] for j in range(len(input))]

def printy(grid):
    for l in grid:
        print(l)

# def dfs(x, y, grid, steps):  
#     if grid[y][x] != ".":
#         if testgrid[y][x] == -1:
#             testgrid[y][x] = steps
#         elif steps < testgrid[y][x]:
#             testgrid[y][x] = steps
#         else:
#             return
#         if 0 <= y <= len(grid) and 0 <= x <= len(grid[0]):
#             newstep = steps + 1
#             if grid[y][x] == "-":
#                 dfs(x + 1, y, grid, newstep)
#                 dfs(x - 1, y, grid, newstep)
#             if grid[y][x] == "|":
#                 dfs(x, y + 1, grid, newstep)
#                 dfs(x, y - 1, grid, newstep)
#             if grid[y][x] == "L":
#                 dfs(x + 1, y, grid, newstep)
#                 dfs(x, y - 1, grid, newstep)
#             if grid[y][x] == "J":
#                 dfs(x, y - 1, grid, newstep)
#                 dfs(x - 1, y, grid, newstep)
#             if grid[y][x] == "F":
#                 dfs(x + 1, y, grid, newstep)
#                 dfs(x, y + 1, grid, newstep)
#             if grid[y][x] == "7":
#                 dfs(x - 1, y, grid, newstep)
#                 dfs(x, y + 1, grid, newstep)
#     else:
#         return
zzz = []
#things =  ["-", "|", "L","J", "F", "7"]
#things =  ["F"]
#things = ["7"]
things = ["-"]
for e in things:
    seen = []
    testgrid = [[-1 for i in range(len(input[0]))] for j in range(len(input))]
    input[starty] = input[starty][:startx] + e + input[starty][startx + 1:]
    steps = 0
    prev_x, prev_y = startx, starty
    stack = deque()
    stack.append((startx,starty, steps, startx, starty))
    seen_area = []
    path = []
    while stack:
        x, y, curr_steps, prev_x, prev_y = stack.pop()
        if 0 <= y <= len(testgrid) and 0 <= x <= len(testgrid[0]):
            if (x, y) not in seen:
                seen.append((x,y))
            else:
                continue
            if input[y][x] != ".": 
                if testgrid[y][x] == -1:
                    testgrid[y][x] = curr_steps
                elif curr_steps < testgrid[y][x]:
                    testgrid[y][x] = curr_steps
                else:
                    continue
                # if input[y][x] == "-":
                #     if prev_x == x - 1:
                #         new_x, new_y = x, y + 1
                #     elif prev_x == x + 1:
                #         new_x, new_y = x, y - 1
                # if input[y][x] == "|":
                #     if prev_y == y - 1:
                #         new_x, new_y = x - 1, y
                #     elif prev_y == y + 1:
                #         new_x, new_y = x + 1, y
                # if (new_x, new_y) not in seen_area:
                #     if (new_x, new_y) != (-1, -1):
                #         if 0 <= new_y < len(input) and 0 <= new_x < len(input[0]):
                #             if input[new_y][new_x] == ".":
                #                 seen_area.append((new_x, new_y))
                # if input[y][x] == "-":
                #     if prev_x == x - 1:
                #         new_x, new_y = x, y - 1
                #     elif prev_x == x + 1:
                #         new_x, new_y = x, y + 1
                # if input[y][x] == "|":
                #     if prev_y == y - 1:
                #         new_x, new_y = x + 1, y
                #     elif prev_y == y + 1:
                #         new_x, new_y = x - 1, y
                # if (new_x, new_y) not in seen_area:
                #     if (new_x, new_y) != (-1, -1):
                #         if 0 <= new_y < len(input) and 0 <= new_x < len(input[0]):
                #             if input[new_y][new_x] == ".":
                #                 seen_area.append((new_x, new_y))
                # if prev_x == x - 1:
                #     new_x, new_y = x, y + 1
                # elif prev_x == x + 1:
                #     new_x, new_y = x, y - 1
                # elif prev_y == y - 1:
                #     new_x, new_y = x - 1, y
                # elif prev_y == y + 1:
                #     new_x, new_y = x + 1, y
                # if (new_x, new_y) not in seen_area:
                #     if (new_x, new_y) != (-1, -1):
                #         if 0 <= new_y < len(input) and 0 <= new_x < len(input[0]):
                #             if testgrid[new_y][new_x] == -1:
                #                 seen_area.append((new_x, new_y))
                # if prev_x == x - 1:
                #     new_x, new_y = x, y - 1
                # elif prev_x == x + 1:
                #     new_x, new_y = x, y + 1
                # elif prev_y == y - 1:
                #     new_x, new_y = x + 1, y
                # elif prev_y == y + 1:
                #     new_x, new_y = x - 1, y
                # if (new_x, new_y) not in seen_area:
                #     if (new_x, new_y) != (-1, -1):
                #         if 0 <= new_y < len(input) and 0 <= new_x < len(input[0]):
                #             if input[new_y][new_x] == ".":
                #                 seen_area.append((new_x, new_y))
                    
                #continue
                if input[y][x] == "-":
                    stack.append((x + 1, y, curr_steps + 1, x, y))
                    stack.append((x - 1, y, curr_steps + 1, x, y))
                if input[y][x] == "|":
                    stack.append((x, y + 1, curr_steps + 1, x, y))
                    stack.append((x, y - 1, curr_steps + 1, x, y))
                if input[y][x] == "L":
                    stack.append((x + 1, y, curr_steps + 1, x, y))
                    stack.append((x, y - 1, curr_steps + 1, x, y))
                if input[y][x] == "J":
                    stack.append((x - 1, y, curr_steps + 1, x, y))
                    stack.append((x, y - 1, curr_steps + 1, x, y))
                if input[y][x] == "F":
                    stack.append((x + 1, y, curr_steps + 1, x, y))
                    stack.append((x, y + 1, curr_steps + 1, x, y))
                if input[y][x] == "7":
                    stack.append((x - 1, y, curr_steps + 1, x, y))
                    stack.append((x, y + 1, curr_steps + 1, x, y))

    #print("")
    print(max([max(i) for i in testgrid]))
    print(e)
    #print(len(seen_area))
    #print(seen_area)
    #print("")
    
    
        

   
    
    totalseens = []

    print(seen[:10], seen[-10::])
    print(len(set(seen)))
    #print(len(seen_area))
    print("")
    offsets = [(-1, -1), (-1,0), (-1, 1), (0,-1), (0, 1), (1, -1), (1, 0), (1,1)]
    # for curr_x,curr_y in seen_area:
    #     stack = deque()
    #     stack.append((curr_x,curr_y))
    #     while stack:
    #         x, y = stack.popleft()
    #         if (x, y) not in newseens:
    #             newseens.append((x,y))
    #             for offset_x, offset_y in offsets:
    #                 nx, ny = x+offset_x, y+offset_y
    #                 if 0 <= ny < len(testgrid) and 0 <= nx < len(testgrid[0]):
    #                     if testgrid[ny][nx] == -1: 
    #                         stack.append((x + offset_x, y + offset_y))
    #         else:
    #             continue
    # print(len(newseens))
prev_x, prev_y = seen[0]
seen_area = []
for i, pair in enumerate(seen):
    x, y = pair
    new_x, new_y = (-1, -1)
    checks = []
    if i < len(seen) - 1:
        next_x, next_y = seen[i + 1]
    else:
        next_x, next_y = startx, starty
    # if prev_x == x + 1:
    #     new_x, new_y = x, y + 1
    #     prev_x, prev_y = prev_x, prev_y + 1
    # elif prev_x == x - 1:
    #     new_x, new_y = x, y - 1
    #     prev_x, prev_y = prev_x, prev_y - 1
    # elif prev_y == y  + 1:
    #     new_x, new_y = x - 1, y
    #     prev_x, prev_y = prev_x - 1, prev_y
    # elif prev_y == y - 1:
    #     new_x, new_y = x + 1, y
    #     prev_x, prev_y = prev_x  + 1, prev_y
    if prev_x == x - 1:
        new_x, new_y = x, y + 1
        prev_x, prev_y = prev_x, prev_y + 1
    elif prev_x == x + 1:
        new_x, new_y = x, y - 1
        prev_x, prev_y = prev_x, prev_y - 1
    elif prev_y == y - 1:
        new_x, new_y = x - 1, y
        prev_x, prev_y = prev_x - 1, prev_y
    elif prev_y == y + 1:
        new_x, new_y = x + 1, y
        prev_x, prev_y = prev_x  + 1, prev_y
    checks.append((new_x, new_y))
    checks.append((prev_x, prev_y))
    for nx, ny in checks:
        new_x, new_y = nx, ny
        if (new_x, new_y) not in seen_area:
            if (new_x, new_y) != (-1, -1):
                if 0 <= new_y < len(input) and 0 <= new_x < len(input[0]):
                    if (new_x, new_y) not in seen:
                        seen_area.append((new_x, new_y))
    prev_x, prev_y = x, y
#seen_area.append((startx, starty))
#print(seen_area)
print(len(seen_area))
newseens = []
for curr_x,curr_y in seen_area:
    stack = deque()
    stack.append((curr_x,curr_y))
    while stack:
        x, y = stack.popleft()
        if (x, y) not in newseens:
            newseens.append((x,y))
            for offset_x, offset_y in offsets:
                nx, ny = x+offset_x, y+offset_y
                if 0 <= ny < len(testgrid) and 0 <= nx < len(testgrid[0]):
                    if testgrid[ny][nx] == -1: 
                        stack.append((x + offset_x, y + offset_y))
        else:
            continue

print(len(newseens))
print((len(testgrid) * len(testgrid[0])))
#print(newseens)
#print(len(seen_area))

#printy(testgrid)
#print(seen)