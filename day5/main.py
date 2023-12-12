seeds = []
dicts = []
with open('input.txt') as f:
    current_dict = 0
    for index, line in enumerate(f):
        if "seeds:" in line.strip().split(" "):
            seeds = [int(i) for i in line.strip().split(" ")[1:]]
        elif "map:" in line.strip().split(" "):
            if current_dict != 0:
                dicts.append(current_dict)
            current_dict = {}
        elif len(line.strip().split(" ")) > 1:
            start, end, range_amt = line.strip().split(" ")
            start, end, range_amt = int(start), int(end), int(range_amt)
            current_dict[(end, end + range_amt - 1)] = (start, start + range_amt - 1)
    dicts.append(current_dict)
print(seeds)
print(dicts)

seed_ranges = []
for i in range(0,len(seeds),2):
    seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))
print(seed_ranges)
    


outputs = []
output = []
#for seed in seeds:
# for seed in seed_ranges:
#     i = 0
#     num = seed
#     path = [num]
#     while i <= len(dicts) - 1:
#         for start, start_end in dicts[i]:
#             if num in range(start, start_end + 1):
#                 num = dicts[i][(start, start_end)][0] + num - start
#                 break
#         i += 1
#         path.append(num)
#     outputs.append(path)
#     output.append(num)
# print(output)
# print(min(output))

# for min, max in seed_ranges:
#     i = 0
#     curr_min, curr_max = min, max
#     path = [num]
#     while i <= len(dicts) - 1:
#         for start, start_end in dicts[i]:
#             if curr_max >= start_end 
#                 num = dicts[i][(start, start_end)][0] + num - start
#                 break
#         i += 1
#         path.append(num)
#     outputs.append(path)
#     output.append(num)
def fill_gaps(lst, min_val, max_val):
    result_list = []
    current_min = min_val
    for l in lst:
        if l[0] > current_min:
            result_list.append((current_min, l[0]-1))
        result_list.append(l)
        current_min = l[1] + 1
    if current_min <= max_val:
        result_list.append((current_min, max_val))
    return result_list

for min, max in seed_ranges:
    overlaps = []
    d = {}
    for start, end in dicts[0]:
        next_start, next_end = dicts[0][(start, end)]
        offset = next_start - start
        if min < start and max < start:
            #do nothing
            continue
        elif min > end and max > end:
            continue
        elif min > start and max > end and min < end:
            overlaps.append((min, end))
            d[(min, end)] = (min + offset, end + offset)
        elif start > min and start < max and end > max:
            overlaps.append((start, max))
            d[(start, max)] = (start + offset, max + offset)
        elif start > min and end > min and start < max and end < max:
            overlaps.append((start, end))
            d[(start, end)] = (start + offset, end + offset)
        elif min > start and max > start and min < end and max < end:
            overlaps.append((min, max))
            d[(min, max)] = (min + offset, max + offset)
    overlaps.sort()
    print("doggis", overlaps)
    print(min, max)
    print(fill_gaps(overlaps, min, max))
            
            