import re

TABLE = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

def get_num_v1(line):
  cs = re.findall(r"\d", line)
  return int(f"{cs[0]}{cs[-1]}")


def get_num_v2(line):
  cs = re.findall(r"\d|" + "|".join([key for key in TABLE]), line)
  cs = [c if len(c) == 1 else TABLE[c] for c in cs]
  print(cs)
  return int(f"{cs[0]}{cs[-1]}")

with open("1.input", "r") as fp:
  data = fp.read()

data = data.split("\n")

n = 0
for line in data:
  n += get_num_v2(line)
print(n)