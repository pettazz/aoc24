import re

with open("input.txt") as f:
  memory = f.read().replace("\n", "")

total = 0
regex = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
for op in re.findall(regex, memory):
  total += int(op[0]) * int(op[1])

print(total)