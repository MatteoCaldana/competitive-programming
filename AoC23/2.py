import functools
import operator

with open("2.input", "r") as fp:
  data = fp.readlines()

RULE = {"red":12, "green": 13, "blue": 14}


def parse_game(game_line):
  game_line = game_line.strip("\n")
  game_line_tokens = game_line.split(": ")
  id = int(game_line_tokens[0].split(" ")[-1])
  rounds = game_line_tokens[1].split("; ")
  rounds = [round.split(", ") for round in rounds]
  rounds = [{pair.split(' ')[1]: int(pair.split(' ')[0]) for pair in round} for round in rounds]
  return {"id": id, "rounds": rounds}

def check_rule(round):
  for color in round:
    if round[color] > RULE[color]:
      return False
  return True

def min_set(game):
  mmin = {"red":0, "green": 0, "blue": 0}
  for round in game["rounds"]:
    for color in round:
      mmin[color] = max(round[color], mmin[color])
  return functools.reduce(operator.mul, mmin.values(), 1)


games = [parse_game(line) for line in data]

sum_ok = 0
sum_min_set = 0
for game in games:
  sum_min_set += min_set(game)
  ok_game = True
  for round in game["rounds"]:
    if not check_rule(round):
      print("IMPOSSIBLE", game["id"])
      ok_game = False
      break
  if ok_game:
    sum_ok += game["id"]


print(sum_ok)
print(sum_min_set)