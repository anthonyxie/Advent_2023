import sys
input = []
print(sys.getrecursionlimit())
sys.setrecursionlimit(6000)
def outofbounds(x, y, grid):
    if not 0 <= y < len(grid) or not 0 <= x < len(grid[0]):
        print("oops ur out")
        return True
    return False

def printy(grid):
    for l in grid:
        print([" " if len(line) == 0 else line[0] for line in l])



with open('input.txt') as f:
    for index, line in enumerate(f):
        line = line.strip()
        input.append([c for c in line])

mem = [[[] for i in mat] for mat in input]

#printy(memgrid)

def beam(x, y, dir, grid):
    

    if outofbounds(x,y,grid):
        return
    if dir in mem[y][x]:
        return
    curr_tile = grid[y][x]
    mem[y][x].append(dir)
    
    if dir == "r":
        if curr_tile == "|":
            beam(x,y - 1, "u",grid)
            beam(x,y + 1, "d",grid)
        elif curr_tile == "\\":
            beam(x, y + 1, "d",grid)
        elif curr_tile == "/":
            beam(x, y - 1, "u",grid)
        else:
            beam(x + 1, y, "r", grid)       
    elif dir == "l":
        if curr_tile == "|":
            beam(x,y - 1, "u",grid)
            beam(x,y + 1, "d",grid)
        elif curr_tile == "\\":
            beam(x,y - 1, "u",grid)
        elif curr_tile == "/":
            beam(x,y + 1, "d",grid)
        else:
            beam(x - 1, y, "l", grid)

    elif dir == "u":
        if curr_tile == "\\":
            beam(x - 1,y, "l",grid)
        elif curr_tile == "/":
            beam(x + 1,y, "r",grid)
        elif curr_tile == "-":
            beam(x + 1,y, "r",grid)
            beam(x - 1,y, "l",grid)
        else:
            beam(x,y - 1, "u",grid)
    elif dir == "d":
        if curr_tile == "\\":
            beam(x + 1,y, "r",grid)
        elif curr_tile == "/":
            beam(x - 1,y, "l",grid)
        elif curr_tile == "-":
            beam(x + 1,y, "r",grid)
            beam(x - 1,y, "l",grid)
        else:
            beam(x,y + 1, "d",grid)

beam(0,0,"r",input)
print(len(input))

output = 0
for i in range(len(mem)):
    for j in range(len(mem[0])):
        if len(mem[i][j]) > 0:
            output += 1
print(output)

