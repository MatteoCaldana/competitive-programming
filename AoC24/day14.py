import re
import numpy as np
import matplotlib.pyplot as plt

with open("input.01.day14", "r") as fp:
    data = fp.read()

matches = re.findall(r"p=(\d+),(\d+) v=([-\d]+),([-\d]+)", data)
matches = [
    [
        np.array([int(m[0]), int(m[1])], dtype=int),
        np.array([int(m[2]), int(m[3])], dtype=int),
    ]
    for m in matches
]
ps = np.stack([m[0] for m in matches])
vs = np.stack([m[1] for m in matches])
ps0 = ps.copy()

for _ in range(100):
    ps = (ps + vs) % np.array([101, 103], dtype=int)

cnt1 = np.where((ps[:, 0] < 101 // 2 ) & (ps[:, 1] < 103 // 2))[0].size
cnt2 = np.where((ps[:, 0] < 101 // 2 ) & (ps[:, 1] > 103 // 2))[0].size
cnt3 = np.where((ps[:, 0] > 101 // 2 ) & (ps[:, 1] < 103 // 2))[0].size
cnt4 = np.where((ps[:, 0] > 101 // 2 ) & (ps[:, 1] > 103 // 2))[0].size

print(cnt1 * cnt2 * cnt3 * cnt4)

ps = ps0
smin = 999
sidx = -1
for _ in range(10000):
    ps = (ps + vs) % np.array([101, 103], dtype=int)
    table = np.zeros((101, 103), dtype=int)
    table[ps[:, 0], ps[:, 1]] = 1
    sv = np.std(table, axis=0).mean()
    sh = np.std(table, axis=1).mean()
    s = sv + sh
    if s < smin:
        smin = s
        sidx = _
    smin = min([smin, s])

print(sidx + 1, s, smin)

