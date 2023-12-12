times = []
records = []
with open('input.txt') as f:
    for index, line in enumerate(f):
        total = 0
        line = line.strip()
        if "Time:" in line.strip().split():
            times = [i for i in line.strip().split(" ")[1:] if len(i) > 0]
        elif len(line.strip().split()) > 1:
            records = [i for i in line.strip().split(" ")[1:] if len(i) > 0]
final = ""
final_rec = ""
for time in times:
    final += time
final = int(final)
for record in records:
    final_rec += record
final = int(final)
final_rec = int(final_rec)
print(final)

# for index, time in enumerate(times):
#     sub = 0
#     for i in range(0, time + 1):
#         if i * (time - i) >= records[index]:
#             sub += 1
#     print(sub)
#     output *= sub
# print(output)

sub = 0
for i in range(0, final + 1):
    if i * (final - i) >= final_rec:
        sub += 1
print(sub)