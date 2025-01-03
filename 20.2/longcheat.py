cross = []
for p in (0, 1):
  for i in (-1, 1):
    n = [0] * 2
    n[p] = i
    cross.append((*n,))
# west, east, north, south

maze = []
start = (0, 0)
end = (0, 0)
with open("input.txt") as f:
  for y, line in enumerate(f):
    row = []
    for x, c in enumerate(line.strip()):
      row.append(c)
      if c == "S":
        start = (x, y)
      if c == "E":
        end = (x, y)
    maze.append(row)
bounds = (len(maze[0]), len(maze))

def mapchar(coord):
  return maze[coord[1]][coord[0]]

def islegal(coord):
  return 0 <= coord[0] < bounds[0] and \
         0 <= coord[1] < bounds[1]

def dist(p1, p2):
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

distmap = {end: 0}
distance = 0
pos = end
while pos != start:
  distance += 1
  for d in cross:
    testpos = (pos[0] + d[0], pos[1] + d[1])
    if testpos not in distmap.keys() and islegal(testpos) and mapchar(testpos) == ".":
      break
  distmap[testpos] = distance
  pos = testpos

shortcuts = []
for step in distmap.keys():
  for jumppos in [pos for pos in distmap.keys() if step != pos and 1 < dist(step, pos) <= 20]:
    cheatDist = dist(step, jumppos)
    saved = (distmap[step] - distmap[jumppos]) - cheatDist
    if saved >= 100:
      shortcuts.append(saved)

print(len(shortcuts))
# import itertools
# print([(c, len(list(grp))) for c, grp in itertools.groupby(sorted(shortcuts))])
