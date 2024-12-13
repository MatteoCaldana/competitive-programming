import re
import bisect

with open("input.01.day03", "r") as fp:
    data = fp.read()

ms = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", data)
sum = 0
for m in ms:
    sum += int(m[0]) * int(m[1])
print(sum)

dos = [(True, 0)] + [(True, x.span()[0]) for x in re.finditer(r"do\(\)", data)]
dns = [(False, x.span()[0]) for x in re.finditer(r"don't\(\)", data)]
dd = dos + dns
dd.sort(key=lambda x:x[1])
d = [x[1] for x in dd]

sum2 = 0
for m in re.finditer(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", data):
    idx = m.span()[0]
    list_idx = bisect.bisect_left(d, idx) - 1
    print(idx, dd[list_idx][0], dd[list_idx][1])
    if dd[list_idx][0]:
        sum2 += int(m.group(1)) * int(m.group(2))
print(sum2)