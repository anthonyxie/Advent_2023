def fill_gaps(lst, min_val, max_val):
    lst.sort()
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

lst = [(2,3),(6,7)]
print(fill_gaps(lst, 0, 10))