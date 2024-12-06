rules = {}
updates = []
middles = 0

def checkupdate(update):
  visited = []
  for page in update:
    if page in rules.keys():
      # now this is pythonic af but going to be tough to translate
      rule = set(rules[page])
      if set(visited).intersection(rule):
        return False

    if page not in visited:
      visited.append(page)
  return True

def fixupdate(update):
  fixed = []
  visited = []
  for page in update:
    if page in rules.keys():
      rule = set(rules[page])
      wrongs = set(visited).intersection(rule)
      if wrongs:
        # wow good thing i put the time into sorting the rules
        fixed.insert(fixed.index(list(wrongs)[-1]), page)
      else:
        fixed.append(page)

    else:
      fixed.append(page)

    visited.append(page)

  return fixed

with open("input.txt") as f:
  for line in f:
    line = line.strip()
    if line == "":
      break
    rule = line.split("|")
    bef = int(rule[0])
    aft = int(rule[1])
    if not bef in rules.keys():
      rules[bef] = [aft]
    else:
      cidx = 0
      while cidx < len(rules[bef]) and rules[bef][cidx] <= aft:
        cidx += 1
      rules[bef].insert(cidx, aft)

  updates = [list(map(int, line.strip().split(","))) for line in f]

for update in updates:
  fixiters = 0 
  while not checkupdate(update):
    update = fixupdate(update)
    fixiters += 1
  if fixiters > 0:
    middles += update[len(update) // 2]

print(middles)