import numpy as np

with open("4.input", "r") as fp:
  data = fp.read().splitlines()

def parse_card(line):
  card, numbers = line.split(": ")
  winning, have = numbers.split(" | ")
  winning = set([int(n) for n in winning.split(" ") if len(n)])
  have = set([int(n) for n in have.split(" ") if len(n)])
  return card, winning, have

cards = [parse_card(line) for line in data]
have_winning = [len(winning & have) for _, winning, have in cards]
value = [2**(n-1) if n > 0 else 0 for n in have_winning]

print(sum(value))

table = np.ones((len(cards, )), dtype=np.int32)
for i, n in enumerate(have_winning):
  table[i+1:i+n+1] += table[i]

print(sum(table))