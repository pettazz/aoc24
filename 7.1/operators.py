total = 0

eqs = []
with open("input.txt") as f:
  for line in f:
    line = line.strip()
    if line == "":
      break
    equation = line.split(":")
    test = int(equation[0])
    vals = [int(num) for num in equation[1].strip().split()]

    eqs.append([test, vals])

def checkvals(total, vals):
  if len(vals) == 1:
    return total == vals[0]

  if total % vals[-1] == 0 and checkvals(total // vals[-1], vals[:-1]):
    return True
  else:
    return checkvals(total - vals[-1], vals[:-1])

for eq in eqs:
  if eq[0] == sum(eq[1]):
    total += eq[0]
    continue

  if checkvals(eq[0], eq[1]):
    total += eq[0]

print(total)