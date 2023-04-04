
f = open("22.txt", 'r')
data = f.read()

names = data.split(',')

for i in range(len(names)):
    if (names[i][0] == '"') and (names[i][-1] == '"'):
        names[i] = names[i][1:-1]
    else:
        print("Warning: bad name", names[i])

names.sort()

def evaluate_name(name):
    val = 0
    for i in range(len(name)):
        val += ord(name[i]) - ord('A') + 1
    return val

print(names[937], evaluate_name(names[937]))

sol = 0
for i in range(len(names)):
    sol += (i + 1) * evaluate_name(names[i])
print(sol)