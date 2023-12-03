import json
input_array = []
combos = []

with open('input.txt') as f:
    for index, line in enumerate(f):
        input_array.append(line.strip())

        start_index = -1
        end_index = -1
        for c_index, c in enumerate(line):
            if c.isnumeric():
                if start_index == -1:
                    start_index = c_index
                    end_index = c_index
                else:
                    end_index = c_index
            elif (start_index != -1 and end_index != -1):
                combos.append((index, start_index, end_index))
                start_index = -1
                end_index = -1



output = 0
offsets = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]
unique_symbols = set()

shared_gear = {}
print(combos)
for index, start, end in combos:
    total = ""
    flag = False
    for i in range(start, end + 1):
        y = index
        x = i
        
        for x_off, y_off in offsets:
            if not flag:
                if 0 <= x + x_off < len(input_array[0]) and 0 <= y + y_off < len(input_array):
                    if not input_array[y + y_off][x + x_off].isalnum():
                        if input_array[y + y_off][x + x_off] != ".":
                            if input_array[y + y_off][x + x_off] == "*":
                                if (y + y_off, x + x_off) not in shared_gear:
                                    shared_gear[(y + y_off, x + x_off)] = []
                                shared_gear[(y + y_off, x + x_off)].append(int(input_array[index][start:end + 1]))
                                flag = True        

    if flag is True:
        print(index, input_array[index][start:end + 1])
        #addtn = int(input_array[index][start:end + 1])
        #output += addtn
print(shared_gear)    
for key in shared_gear:
    if len(shared_gear[key]) == 2:
        mult = shared_gear[key][0] * shared_gear[key][1]
        output += mult

print(output)
        




            
    
