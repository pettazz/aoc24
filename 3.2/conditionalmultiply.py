import re

with open("input.txt") as f:
  memory = f.read().replace("\n", "")

def domuls(block):
  total = 0
  regex = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
  for op in re.findall(regex, block):
    total += int(op[0]) * int(op[1])
  return total

blocks = []
dos = [chunk for chunk in memory.split("do()")]
for do in dos:
  donts = do.split("don't()", 1)
  blocks += [chunk for chunk in donts[:1]]

total = sum(domuls(block) for block in blocks)
print(total)