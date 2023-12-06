# n = secolds hold down start
# s = space
# t = time
# t = n + s / n
# s = nt - n^2
# t given, constraints s > s0, s0 given
# n^2 - nt + s0 = 0
# n_1,2 = (t +/- sqrt(t^2 - 4 s0)) / 2

import re
import math

with open("6.input", "r") as fp:
  data = fp.readlines()


def solve(times, dists):
  assert len(times) == len(dists)

  sol = 1
  for i in range(len(times)):
    s0 = dists[i]
    t = times[i]
    delta = (t*t - 4 * s0)**0.5
    n1 = (t - delta) / 2
    n2 = (t + delta) / 2

    n1 = math.ceil(n1) if math.ceil(n1) != n1 else math.ceil(n1) + 1
    n2 = math.floor(n2) if math.floor(n2) != n2 else math.floor(n2) - 1

    sol *= math.floor(n2) - math.ceil(n1) + 1

  print("sol:", sol)
  
def parse_v1(data):
  times = [float(n) for n in re.findall(r"\d+", data[0])]
  dists = [float(n) for n in re.findall(r"\d+", data[1])]
  return times, dists

def parse_v2(data):
  for i in range(len(data)):
    data[i] = re.sub(" ", "", data[i])
  times = [float(n) for n in re.findall(r"\d+", data[0])]
  dists = [float(n) for n in re.findall(r"\d+", data[1])]
  return times, dists

solve(*parse_v1(data))
solve(*parse_v2(data))
