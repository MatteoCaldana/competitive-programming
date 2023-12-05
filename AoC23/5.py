with open("5.input", "r") as fp:
  data = fp.read()

data = data.split("\n\n")
seeds = [int(x) for x in data[0].split(": ")[1].split(" ")]
raw_tables = data[1:]

def parse_table(lines):
  ranges = []
  lines = lines.splitlines()
  for line in lines[1:]:
    ranges.append([int(x) for x in line.split(' ')])
  return lines[0], ranges

def build_implicit_table(raw_tables):
  tables = []
  for table in raw_tables:
    _, parsed_table = parse_table(table)
    tables.append(parsed_table)
  return tables

def build_explicit_table(implicit_tables, seeds):
  tables = []
  to_build = seeds
  for itable in implicit_tables:
    table = {}
    for seed in to_build:
      table[seed] = seed
      for range in itable:
        if seed >= range[1] and seed < (range[1] + range[2]):
          table[seed] = range[0] + seed - range[1]
          break
    tables.append(table)
    to_build = table.values()
  return tables


def sol_part_1(raw_tables, seeds):
  itables = build_implicit_table(raw_tables)
  etables = build_explicit_table(itables, seeds)

  mmin = 2**64
  for seed in seeds:
    curr = seed
    for table in etables:
      curr = table[curr]
    if curr < mmin:
      mmin = curr

  print("sol1:", mmin)

sol_part_1(raw_tables, seeds)


def range_intersect(range, irange):
  is_min_inside = irange[0] >= range[0] and irange[0] < (range[0] + range[1])
  is_max_inside = (irange[0] + irange[1] - 1) >= range[0] and (irange[0] + irange[1] - 1) < (range[0] + range[1])
  if is_min_inside:
    if is_max_inside:
      return (irange[0], irange[1]), [(range[0], irange[0] - range[0]), (irange[0] + irange[1], range[0] + range[1] - (irange[0] + irange[1]))]
    else:
      return (irange[0], range[0] + range[1] - irange[0]), [(range[0], irange[0] - range[0])]
  else:
    if is_max_inside:
      return (range[0], irange[0] + irange[1] - range[0]), [(irange[0] + irange[1], range[0] + range[1] - (irange[0] + irange[1]))]
    else:
      if irange[0] < range[0] and (irange[0] + irange[1] - 1) > (range[0] + range[1]):
        return range, [] 
      return (), [range]
      

def build_explicit_table_v2(implicit_tables, ranges):
  tables = []
  to_build = ranges
  for itable in implicit_tables:
    table = {}
    for range in to_build:
      range = [range] 
      for irange in itable:
        if len(range) == 0:
          break
        for subrange in range:
          intersect, other = range_intersect(subrange, (irange[1], irange[2]))
          if len(intersect):
            table[intersect] = (intersect[0] - irange[1] + irange[0], intersect[1])
            range = [o for o in other if o[1]]

      for subrange in range:
        table[subrange] = subrange

    tables.append(table)
    to_build = table.values()
  return tables

itables = build_implicit_table(raw_tables)
seeds_ranges = list(zip(*[iter(seeds)] * 2))
etables = build_explicit_table_v2(itables, seeds_ranges)

print("sol2:", min([x[0] for x in etables[-1].values()]))