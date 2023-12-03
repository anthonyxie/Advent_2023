import re
def replaceallnumbers(s, firstindex):
    lowest_index = len(s) - 1
    highest_index = -1
    lowest_num = 0
    highest_num = 0
    d = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for num in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
        ind = s.find(num)
        
        if ind != -1:
            if ind < lowest_index:
                lowest_index = ind
                lowest_num = num
    if lowest_num in d and firstindex >= lowest_index:
        s = s.replace(lowest_num, d[lowest_num])
    for num in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
        ind = s.rfind(num)
        if ind != -1:
            if ind > highest_index:
                highest_index = ind
                highest_num = num
    if highest_num in d:
        s = s.replace(highest_num, d[highest_num])
    return s
        
with open('input.txt') as f:
    output = []
    for line in f:
        firstnum = ""
        secondnum = ""
        firstindex = -1
        secondindex = -1
        print(line)
        for index, c in enumerate(line):
            if c.isnumeric():
                if len(firstnum) == 0:
                    firstnum, secondnum = c,c
                    firstindex, secondindex = index, index 
                else:
                    secondnum = c
                    secondindex = index
        line = replaceallnumbers(line, firstindex)
        print(line)
        firstnum = ""
        secondnum = ""
        for index, c in enumerate(line):
            if c.isnumeric():
                if len(firstnum) == 0:
                    firstnum = c
                    secondnum = c
                else:
                    secondnum = c
        combined = firstnum + secondnum
        print(combined)
        output.append(int(combined))
    print(sum(output))
