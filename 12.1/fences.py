cross = []
for p in (0, 1):
  for i in (-1, 1):
    n = [0] * 2
    n[p] = i
    cross.append((*n,))

themap = []
with open("input.txt") as f:
  for row, line in enumerate(f):
    maprow = []
    for col, char in enumerate(line.strip()):
      maprow.append(char)
    themap.append(maprow)
bounds = (len(themap), len(themap[0]))

def inbounds(pos):
  return (0 <= pos[0] < bounds[0]) and (0 <= pos[1] < bounds[1])

def search(pos, seen):
  if pos in seen.keys():
    return []
  crop = themap[pos[0]][pos[1]]
  edges = 0
  for dy, dx in cross:
    testpos = (pos[0] + dy, pos[1] + dx)
    if inbounds(testpos) and themap[testpos[0]][testpos[1]] == crop:
      search(testpos, seen)
    else:
      edges += 1
    seen[pos] = edges
  return seen

visited = set()
total = 0
for y, row in enumerate(themap):
  for x, col in enumerate(row):
    if (y, x) not in visited:
      plot = {}
      plot = search((y, x), {})
      visited.update(list(plot.keys()))
      total += len(plot.keys()) * sum(plot.values())

print(total)