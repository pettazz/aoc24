directions = ["^", ">", "v", "<"]
dirchanges = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Guard:
  def __init__(self, row, col, face):
    self.row = row
    self.col = col
    self.face = face #index of directions
    self.stepsTaken = 1 #initial space counts

  def _rotate(self):
    self.face = (self.face + 1) % 4

  def _getNextValidStep(self, themap, attempts=0):
    assert attempts < 4, "I'm trapped!"
    nextrow = self.row + dirchanges[self.face][0]
    nextcol = self.col + dirchanges[self.face][1]
    nextspot = themap[nextrow][nextcol]
    if nextspot == "#":
      self._rotate()
      return self._getNextValidStep(themap, attempts+1)
    return (nextrow, nextcol)

  def step(self, themap):
    nextpos = self._getNextValidStep(themap)
    if themap[nextpos[0]][nextpos[1]] != 'X':
      self.stepsTaken += 1
    themap[nextpos[0]][nextpos[1]] = directions[self.face]
    themap[self.row][self.col] = 'X'
    self.row = nextpos[0]
    self.col = nextpos[1]
  
themap = []
with open("input.txt") as f:
  for row, line in enumerate(f):
    maprow = []
    for col, char in enumerate(line.strip()):
      if char in directions:
        guard = Guard(row, col, directions.index(char))
      maprow.append(char)
    themap.append(maprow)

while 0 < guard.row < len(themap[0]) - 1 and 0 < guard.col < len(themap) - 1:
  guard.step(themap)

# for row in themap:
#   print(''.join(row))

print(guard.stepsTaken)