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
  return 0 <= coord[0] <= bounds[0] and \
         0 <= coord[1] <= bounds[1]

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

maxdist = distmap[start]
shortcuts = 0
for step in distmap.keys():
  for d in cross:
    skippos = (step[0] + d[0], step[1] + d[1])
    jumppos = (step[0] + (2 * d[0]), step[1] + (2 * d[1]))
    if islegal(skippos) and mapchar(skippos) == "#" and islegal(jumppos) and jumppos in distmap.keys():
      saved = (distmap[step] - distmap[jumppos]) - 2 # offset counting the time of the skip itself (2)
      if saved >= 100:
        shortcuts += 1

print(shortcuts)
# print([(c, len(list(grp))) for c, grp in itertools.groupby(sorted(shortcuts))])
