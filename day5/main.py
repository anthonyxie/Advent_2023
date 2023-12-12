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
#print(dicts)

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

output = []
for min_val, max_val in seed_ranges:
    overlaps = [(min_val, max_val)]
    i = 0
    while i <= len(dicts) - 1:
        d = {}
        all_overlaps = []
        for min_val, max in overlaps:
            new_overlaps = []
            for start, end in dicts[i]:
                next_start, next_end = dicts[i][(start, end)]
                offset = next_start - start
                if min_val < start and max < start:
                    continue
                elif min_val > end and max > end:
                    continue
                elif min_val > start and max > end and min_val < end:
                    new_overlaps.append((min_val, end))
                    d[(min_val, end)] = (min_val + offset, end + offset)
                elif start > min_val and start < max and end > max:
                    new_overlaps.append((start, max))
                    d[(start, max)] = (start + offset, max + offset)
                elif start > min_val and end > min_val and start < max and end < max:
                    new_overlaps.append((start, end))
                    d[(start, end)] = (start + offset, end + offset)
                elif min_val > start and max > start and min_val < end and max < end:
                    new_overlaps.append((min_val, max))
                    d[(min_val, max)] = (min_val + offset, max + offset)
            new_overlaps.sort()
            new_overlaps = fill_gaps(new_overlaps, min_val, max)
            for ind, overlap in enumerate(new_overlaps):
                if overlap in d:
                    new_overlaps[ind] = d[overlap]
            all_overlaps += new_overlaps
        overlaps = all_overlaps
        i += 1
    print(overlaps)
    output.append(min([ol[0] for ol in overlaps]))
print(min(output))
            
            