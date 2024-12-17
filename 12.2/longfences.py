cross = []
for p in (0, 1):
  for i in (-1, 1):
    n = [0] * 2
    n[p] = i
    cross.append((*n,))
# north, south, west, east

exx = [(x, y) for x in (-1, 1) for y in (-1, 1)]
# nw, ne, sw, se

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
  # find corners
  corners = 0
  # index of exx to check against adjacent sides
  ix = 0
  # compare n + w,e and south + w,e (see cross def above)
  for p in (0, 1): # north, south
    for q in (2,3): # west, east
      d1 = cross[p]
      d2 = cross[q]

      d1pos = (pos[0] + d1[0], pos[1] + d1[1])
      d2pos = (pos[0] + d2[0], pos[1] + d2[1])
      d1val = themap[d1pos[0]][d1pos[1]] if inbounds(d1pos) else 'out'
      d2val = themap[d2pos[0]][d2pos[1]] if inbounds(d2pos) else 'out'

      # compare sides to find corners pointing outward
      if d1val != crop and d2val != crop:
        corners += 1

      # compare the sides with the relevant diagonal
      # to find corners pointing inward
      diagpos = (pos[0] + exx[ix][0], pos[1] + exx[ix][1])
      diagval = themap[diagpos[0]][diagpos[1]] if inbounds(diagpos) else 'nope'
      if diagval != crop and d1val == crop and d2val == crop:
        corners += 1

      ix += 1

  for dy, dx in cross:
    testpos = (pos[0] + dy, pos[1] + dx)

    if inbounds(testpos) and themap[testpos[0]][testpos[1]] == crop:
      search(testpos, seen)
    
    seen[pos] = corners
  return seen

visited = set()
total = 0
for y, row in enumerate(themap):
  for x, col in enumerate(row):
    if (y, x) not in visited:
      plot = {}
      plot = search((y, x), {})
      visited.update(list(plot.keys()))
      area = len(plot.keys())
      corners = sum(plot.values())

      # print("plot", col, plot)
      # print("area", area)
      # print("corners", corners)
      total += area * corners

print(total)