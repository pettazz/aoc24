themap = []
heads = []

cross = []
for p in (0, 1):
  for i in (-1, 1):
    n = [0] * 2
    n[p] = i
    cross.append((*n,))

with open("input.txt") as f:
  for row, line in enumerate(f):
    maprow = []
    for col, char in enumerate(line.strip()):
      if int(char) == 0:
        heads.append((row, col))
      maprow.append(int(char))
    themap.append(maprow)
bounds = (len(themap), len(themap[0]))

def inbounds(pos):
  return (0 <= pos[0] < bounds[0]) and (0 <= pos[1] < bounds[1])

def search(pos):
  ends = 0
  height = themap[pos[0]][pos[1]]
  if height == 9:
    return 1
  for dy, dx in cross:
    testpos = (pos[0] + dy, pos[1] + dx)
    if inbounds(testpos):
      if themap[testpos[0]][testpos[1]] == height + 1:
        ends += search(testpos)
  return ends


paths = 0
for head in heads:
  paths += search(head)

print(paths)