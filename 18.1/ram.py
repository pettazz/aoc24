from dataclasses import dataclass

cross = []
for p in (0, 1):
  for i in (-1, 1):
    n = [0] * 2
    n[p] = i
    cross.append((*n,))
# west, east, north, south

@dataclass
class Node:
  coord: tuple
  f: int = None
  g: int = None
  h: int = None
  parent: 'Node' = None

# infile = "test.txt"
# bounds = (6, 6)
# bytemax = 12
infile = "input.txt"
bounds = (70, 70)
bytemax = 1024

maze = []
for y in range(bounds[1] + 1):
  row = ["."] * (bounds[0]+1)
  maze.append(row)
start = Node((0, 0))
end = Node(bounds)

with open(infile) as f:
  for count, line in enumerate(f):
    if count == bytemax:
      break
    if line.strip() == "":
      continue
    coord = (*[int(x) for x in line.strip().split(",")],)
    maze[coord[1]][coord[0]] = "#"

def islegal(coord):
  return 0 <= coord[0] <= bounds[0] and \
         0 <= coord[1] <= bounds[1] and \
         maze[coord[1]][coord[0]] != "#"

def printmaze(path = None):
  for y, mrow in enumerate(maze):
    row = ""
    for x, char in enumerate(mrow):
      if path and (x, y) in path:
        row += "O"
      else:
        row += char
    print(row)

def neighbors(pos):
  neighs = []
  for step in cross:
    testcoord = pos.coord[0] + step[0], pos.coord[1] + step[1]
    if islegal(testcoord):
      neighs.append(testcoord)

  return neighs

def cost(start, end):
  return abs(start[0] - end[0]) + abs(start[1] - end[1])

def pathto(pos):
  path = []
  if pos is None:
    return path
  else:
    return  pathto(pos.parent) + [pos.coord]

start.g = 0
start.h = cost(start.coord, end.coord)
start.f = start.h

path = []
todo = [start]
seencoords = set()

while len(todo) > 0:
  pos = todo.pop()
  
  if pos.coord == end.coord:
    path = pathto(pos)
    break

  seencoords.add(pos.coord)

  for neighcoord in neighbors(pos):
    if neighcoord in seencoords:
      continue

    neighbor = Node(neighcoord)
    neighbor.g = pos.g + cost(pos.coord, neighbor.coord)
    neighbor.h = cost(neighbor.coord, end.coord)
    neighbor.f = neighbor.g + neighbor.h
    neighbor.parent = pos

    oldneighbor = next((n for n in todo if n.coord == neighbor.coord),  None)

    if oldneighbor is None:
      idx = 0
      for f, todopos in enumerate(todo):
        if todopos.f <= neighbor.f:
          idx = f
          break
      todo.insert(idx, neighbor)
      
    elif neighbor.f < oldneighbor.f:
      todo[todo.index(oldneighbor)] = neighbor

printmaze(path)
print(len(path)-1)