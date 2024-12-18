import re

with open("input.01.day17", "r") as fp:
    data = fp.read()

A, B, C, *program = [int(x) for x in re.findall(r"(\d+)", data)]


def solve(A, B, C, program):
    output = []
    iptr = 0
    while iptr < len(program):
        literal = program[iptr + 1]
        combo = [0, 1, 2, 3, A, B, C][literal]
        match program[iptr]:
            case 0: 
                A = A // (1 << combo)
            case 1: 
                B = B ^ literal
            case 2:
                B = combo % 8
            case 3:
                if A != 0:
                    iptr = literal - 2
            case 4:
                B = B ^ C
            case 5:
                output.append(combo % 8)
            case 6:
                B = A // (1 << combo)
            case 7: 
                C = A // (1 << combo)

        iptr += 2
    return output

output = solve(A, B, C, program)
print(",".join([str(x) for x in output]))

A = 1
while len(solve(A, B, C, program)) < 15:
    A *= 2

print(A, len(solve(A, B, C, program)))

A = 1
while len(solve(A, B, C, program)) < 17:
    A *= 2
print(A, len(solve(A, B, C, program)))
