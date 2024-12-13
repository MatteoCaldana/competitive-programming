import re
import numpy as np

with open("input.01.day04", "r") as fp:
    raw_data = fp.read()

def tostr(x):
    return ''.join([*x.reshape((-1,))])

idx = raw_data.find("\n")
raw_data = raw_data + (" " * (idx + 1))

hh = len(re.findall("XMAS", raw_data))
hr = len(re.findall("XMAS", raw_data[::-1]))

data = np.array([x for x in raw_data]).reshape((-1, idx + 1))
dataT = tostr(data.T)
vv = len(re.findall("XMAS", dataT))
vr = len(re.findall("XMAS", dataT[::-1]))

assert(data.shape[0] == data.shape[1])

dataD = tostr(np.diag(data, 0))
datalr = np.fliplr(data)
dataDD = tostr(np.diag(datalr, 0))

for i in range(1, data.shape[0]):
    dataD += tostr(np.diag(data, i))
    dataD += tostr(np.diag(data, -i))
    dataDD += tostr(np.diag(datalr, i))
    dataDD += tostr(np.diag(datalr, -i))

dd = len(re.findall("XMAS", dataD))
dr = len(re.findall("XMAS", dataD[::-1]))
ii = len(re.findall("XMAS", dataDD))
ir = len(re.findall("XMAS", dataDD[::-1]))

print(hh, hr, vv, vr, dd, dr, ii, ir)

print(hh + hr + vv + vr + dd + dr + ii + ir)

raw_data = raw_data.replace("\n", " ")

print(raw_data)
cnt = 0
cnt += len(re.findall(r"(?=(M[^ ]S.{139}A.{139}M[^ ]S))", raw_data))
cnt += len(re.findall(r"(?=(S[^ ]S.{139}A.{139}M[^ ]M))", raw_data))
cnt += len(re.findall(r"(?=(M[^ ]M.{139}A.{139}S[^ ]S))", raw_data))
cnt += len(re.findall(r"(?=(S[^ ]M.{139}A.{139}S[^ ]M))", raw_data))
print(cnt)