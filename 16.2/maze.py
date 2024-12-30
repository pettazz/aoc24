from dataclasses import dataclass

cross = []
for p in (0, 1):
  for i in (-1, 1):
    n = [0] * 2
    n[p] = i
    cross.append((*n,))
# west, east, north, south

def dirtx(d):
  # aligns with cross above
  # because i wanted to be cute and use strings instead
  dirs = ["<", ">", "^", "v"]
  return cross[dirs.index(d)]

@dataclass
class Node:
  coord: tuple
  score: int = None
  parent: 'Node' = None

  @property
  def flatcoord(self):
    return (self.coord[0], self.coord[1])

maze = []
start = Node((0, 0))
end = (0, 0)
with open("test.txt") as f:
  for y, line in enumerate(f):
    row = []
    for x, c in enumerate(line.strip()):
      row.append(c)
      if c == "S":
        start.coord = (x, y, ">")
      if c == "E":
        end = (x, y)
    maze.append(row)

def islegal(coord):
  return maze[coord[1]][coord[0]] != "#"

def printmaze(paths):
  for y, mrow in enumerate(maze):
    row = ""
    for x, char in enumerate(mrow):
      pathval = next((n for n in paths if (n[0], n[1]) == (x, y)),  None)
      if pathval:
        if char == "#":
          row += "!"
        else:
          row += "O"
      else:
        row += char
    print(row)
  
def neighbors(pos):
  neighs = []
  # take a step in the direction we're facing
  stepdir = dirtx(pos.coord[2])
  testcoord = pos.coord[0] + stepdir[0], pos.coord[1] + stepdir[1], pos.coord[2]
  if islegal(testcoord):
    neighs.append(testcoord)

  # or turn 90deg
  turndirs = ["^", ">", "v", "<"]
  facing = turndirs.index(pos.coord[2])
  for turn in [turndirs[(facing + 1) % 4], turndirs[facing -1]]:
    # why didnt i just use the damn tuples god
    testcoord = (pos.coord[0], pos.coord[1], turn)
    if islegal(testcoord):
      neighs.append(testcoord)

  return neighs

def pathto(pos):
  if pos is None:
    return set()
  else:
    paths = pathto(pos.parent)
    paths.update([pos.flatcoord])
    return paths

start.score = 0

paths = set()
winningscore = None
todo = [start]
scoredcoords = {}

while len(todo) > 0:
  pos = todo.pop()
  score = pos.score

  if winningscore and score < winningscore:
    break
  
  if pos.flatcoord == end:
    winningscore = score
    paths |= pathto(pos)
    continue

  if pos.coord in scoredcoords.keys():
    if score < scoredcoords[pos.coord]:
      continue
  scoredcoords[pos.coord] = score

  for neighcoord in neighbors(pos):

    neighbor = Node(neighcoord)
    neighbor.score = pos.score + (1000 if pos.coord[2] != neighbor.coord[2] else 1)
    neighbor.parent = pos

    if neighbor.coord in scoredcoords.keys():
      if neighbor.score >= scoredcoords[neighbor.coord]:
        continue
    scoredcoords[neighbor.coord] = neighbor.score

    oldneighbor = next((n for n in todo if n.coord == neighbor.coord),  None)

    if oldneighbor is None:
      idx = 0
      for f, todopos in enumerate(todo):
        if todopos.score <= neighbor.score:
          idx = f
          break
      todo.insert(idx, neighbor)
      
    elif neighbor.score < oldneighbor.score:
      todo[todo.index(oldneighbor)] = neighbor

printmaze(paths)
print(len(paths))
