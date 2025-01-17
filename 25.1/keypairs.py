MAXHEIGHT = 5
locks = []
keys = []
with open("input.txt") as f:
  parsing = None
  for line in f:
    if parsing is not None:
      if line.strip() == "":
        if parsing == "lock":
          locks.append(current)
        if parsing == "key":
          keys.append(current)
        parsing = None

      for pos, char in enumerate(line.strip()):
        if parsing == "lock" and char == "#":
          current[pos] += 1
        if parsing == "key" and char == ".":
          current[pos] = current[pos] - 1
    else:
      if line.strip() == ".....":
        parsing = "key"
        current = [5] * 5
      if line.strip() == "#####":
        parsing = "lock"
        current = [0] * 5
  
  if parsing == "lock":
    locks.append(current)
  if parsing == "key":
    keys.append(current)

fits = 0
for key in keys:
  for lock in locks:
    if all([key[i] + lock[i] <= MAXHEIGHT for i in range(len(key))]):
      fits += 1
print(fits)