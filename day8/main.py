import math
input_array = []
directions = ""
d = {}
with open('input.txt') as f:
    for index, line in enumerate(f):
        if index == 0:
            directions = line.strip()
        elif "=" in line:
            start = line.split(" ")[0]
            left = line.split(" ")[2][1:4]
            right = line.split(" ")[3][0:3]
            d[start] = (left, right)

curr_loc = "AAA"
i = 0
print(d)
while curr_loc != "ZZZ":
    for direction in directions:
        if curr_loc == "ZZZ":
            break
        if direction == "L":
            curr_loc = d[curr_loc][0]
        elif direction == "R":
            curr_loc = d[curr_loc][1]
        i += 1

curr_locations = [i for i in d.keys() if i.endswith("A")]
print(curr_locations)
dc = {}
ee = []
for curr_loc in curr_locations:
    i = 0
    while not curr_loc.endswith("Z"):
        for direction in directions:
            if curr_loc.endswith("Z"):
                break
            if direction == "L":
                curr_loc = d[curr_loc][0]
            elif direction == "R":
                curr_loc = d[curr_loc][1]
            i += 1
    ee.append(i)
print(ee)


print(math.lcm(*ee))

# def checkAllTrue(list):
#     return False not in list

# def checkA(s):
#     return s.endswith("A")

# def checkZ(s):
#     return s.endswith("Z")
# i = 0
# while not checkAllTrue(list(map(checkZ, curr_locations))):
#     for direction in directions:
#         if checkAllTrue(list(map(checkZ, curr_locations))):
#             break
#         for index, curr_location in enumerate(curr_locations):
#             if direction == "L":
#                 curr_locations[index] = d[curr_location][0]
#             elif direction == "R":
#                 curr_locations[index] = d[curr_location][1]
#         i += 1
#         print(curr_locations)
# print(i)
    