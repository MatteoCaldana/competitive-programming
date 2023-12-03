with open("3.input", "r") as fp:
  data = fp.read().splitlines()

n = len(data)
m = len(data[0])

def get_nums():
  nums = []
  for i in range(n):
    j = 0
    while j < m:
      if data[i][j].isdigit():
        num_start = j
        num_end = 0
        for k in range(1, m - j):
          if not data[i][j + k].isdigit():
            num_end = j + k
            break
        if num_end == 0:
          num_end = m
        nums.append((i, num_start, num_end))
        j = num_end
      else:
        j += 1
  return nums

def inside(i, j):
  return i >= 0 and j >= 0 and i < n and j < m

def check(i, j):
  if inside(i, j):
    if (not data[i][j].isdigit()) and (data[i][j] != '.'):
      return True
  return False


def find_ok_nums(nums):
  ok_nums = []
  for num in nums:
    i, s, e = num

    ok = False
    for j in range(s-1, e+1):
      if ok:
        break
      for di in [-1, 1]:
        if check(di + i, j):
          ok = True
          break

    ok = ok or check(i, s - 1) or check(i, e)

    if ok:
      ok_nums.append((num, int(data[i][s:e])))
  return ok_nums
      
nums = get_nums()

def part_1_sol(): 
  ok_nums = find_ok_nums(nums)
  sol = sum([x[-1] for x in ok_nums])
  print(sol)

part_1_sol()

def gear(i, j):
  return inside(i, j) and data[i][j] == "*"

def find_gears(nums):
  gears = {}
  for num in nums:
    i, s, e = num
    gears[num] = []

    for j in range(s-1, e+1):
      for di in [-1, 1]:
        if gear(di + i, j):
          gears[num].append((di + i, j))
    
    for j in [s - 1, e]:
      if gear(i, j):
        gears[num].append((i, j))

    if len(gears[num]) == 0:
      del gears[num]
  return gears


def reverse_gears(gears):
  table_rev_gear = {}
  for num in gears:
    for gear in gears[num]:
      if gear in table_rev_gear:
        table_rev_gear[gear].add(num)
      else:
        table_rev_gear[gear] = {num}
  return table_rev_gear

gears = find_gears(nums)
reverse_gear_table = reverse_gears(gears)

couples = [list(reverse_gear_table[g]) for g in reverse_gear_table if len(reverse_gear_table[g]) == 2]
couples_ratio = []
for couple in couples:
  ratio = 1
  for i, s, e in couple:
    ratio *= int(data[i][s:e])
  couples_ratio.append(ratio)

print(sum(couples_ratio))