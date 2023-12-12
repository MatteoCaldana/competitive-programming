import numpy as np
import re

with open("12.input", "r") as fp:
    data = fp.read().strip("\n").splitlines()


def parse(line):
    arrangement, expect = line.split(" ")
    expect = [int(n) for n in expect.split(",")]
    return arrangement, expect


def solve_naive(arrangement, expect):
    arrangement = np.array([ord(c) for c in arrangement], dtype=np.int8)
    idx_tofill = np.where(arrangement == ord("?"))[0]
    tot = 0
    for i in range(2**idx_tofill.size):
        re_pattern = (
            r"\.*"
            + "".join([rf"#{{{e}}}\.+" for e in expect[:-1]])
            + rf"#{{{expect[-1]}}}\.*"
        )
        tot += test_arrangement(arrangement, idx_tofill, i, re_pattern)
    return tot


def test_arrangement(arrangement, idx_tofill, fill, re_pattern):
    for i in range(idx_tofill.size):
        arrangement[idx_tofill[i]] = ord("#") if (fill & (1 << i)) > 0 else ord(".")
    s = "".join([chr(c) for c in arrangement])
    m = re.fullmatch(re_pattern, s)
    return bool(m)


def solve_recursive(arrangement, expect):
    if len(expect) == 0:
        if arrangement.find("#") == -1:
            return 1
        else:
            return 0

    quantifier = "+" if len(expect) > 1 else "*"
    has_match = re.match(rf"^\.*#{{{expect[0]}}}\."+quantifier, arrangement)
    if has_match:
        n = has_match.span()[1]
    else:
        n = 0
    has_match = int(bool(has_match))

    print(arrangement, n, has_match)

    if has_match:
        if n == len(arrangement):
            if len(expect) == 1:
                return 1
            else:
                return 0
        else:
            return solve_recursive(arrangement[n:], expect[1:])
    else:
        idx = arrangement.find("?")
        if idx != -1:
            dot = arrangement[:idx] + "." + arrangement[idx + 1 :]
            hsh = arrangement[:idx] + "#" + arrangement[idx + 1 :]
            return solve_recursive(dot, expect) + solve_recursive(hsh, expect)
        else:
            return 0


N = 5
sol = 0
for i, line in enumerate(data):
    arr, exp = parse(line)
    arr = "?".join([arr]*N)
    exp = exp * N
    print(f"{arr} {','.join([str(n) for n in exp])}")
    # print(arr, exp)
    # s = solve_recursive(arr, exp)
    # print(i, s)