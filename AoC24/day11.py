from collections import defaultdict

with open("input.01.day11", "r") as fp:
    data = fp.read()

data = data.split(" ")
data = [int(d) for d in data]
print(data)

def blink(data):
    new_data = []
    for number in data:
        if number == 0:
            new_data.append(1)
        elif len(str(number)) % 2 == 0:
            nstr = str(number)
            new_data.append(int(nstr[:len(nstr)//2]))
            new_data.append(int(nstr[len(nstr)//2:]))
        else:
            new_data.append(number * 2024)
    return new_data

def blink_v2(data):
    new_data = defaultdict(lambda: 0)
    for number in data:
        if number == 0:
            new_data[1] += data[number]
        elif len(str(number)) % 2 == 0:
            nstr = str(number)
            new_data[int(nstr[:len(nstr)//2])] += data[number]
            new_data[int(nstr[len(nstr)//2:])] += data[number]
        else:
            new_data[number * 2024] += data[number]
    return new_data


dd = defaultdict(lambda: 0)
for d in data:
    dd[d] += 1

print(dd)

for i in range(75):
    dd = blink_v2(dd)
    print(i)


print(sum(dd.values()))