doggis = []
with open('input.txt') as f:
    for index, line in enumerate(f):
        line = line.strip()
        doggis = line.split(",")

output = 0
def doggis_hash(hashcode):
    curr = 0
    for c in hashcode:
        curr += ord(c)
        curr *= 17
        curr = curr % 256
    return curr

#part 1
# for hashcode in doggis:
#     output += doggis_hash(hashcode)
d = {}
for i in range(256):
    d[i] = []

for hashcode in doggis:
    if "-" in hashcode:
        label, num = hashcode.split("-")
        code = doggis_hash(label)
        codey_schwab = label
        for i, dog in enumerate(d[code]):
            if codey_schwab in dog:
                del d[code][i]

    if "=" in hashcode:
        flag = False
        label, num = hashcode.split("=")
        code = doggis_hash(label)
        codey_schwab = label + " " + num
        for i, dog in enumerate(d[code]):
            if label in dog:
                d[code][i] = codey_schwab
                flag = True
        if not flag:   
            d[code].append(codey_schwab)

    print([(key, d[key]) for key in d if len(d[key]) > 0])

output = 0
for k, dk in [(key, d[key]) for key in d if len(d[key]) > 0]:
    for index, thing in enumerate(dk):
        num = int(thing.split(" ")[1])
        output += (k+1) * (index+1) * num
print(output)
