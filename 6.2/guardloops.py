directions = ["^", ">", "v", "<"]
dirchanges = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Guard:
  def __init__(self, row, col, face):
    self.row = row
    self.col = col
    self.face = face #index of directions

    self.stepsTaken = 1 #initial space counts
    self.bonks = []

  def rotate(self):
    self.face = (self.face + 1) % 4

  def getNextStepPos(self, mymap):
    nextrow = self.row + dirchanges[self.face][0]
    nextcol = self.col + dirchanges[self.face][1]
    return (nextrow, nextcol)

  def getNextValidStep(self, mymap, attempts=0):
    if attempts > 3:
      raise GuardStuckError()
    nextpos = self.getNextStepPos(mymap)
    nextspot = mymap[nextpos[0]][nextpos[1]]
    if nextspot == "#":
      bonk = (nextpos[0], nextpos[1], self.face)
      if bonk in self.bonks:
        raise GuardLoopError()
      else:
        self.bonks.append(bonk)
      self.rotate()
      return self.getNextValidStep(mymap, attempts+1)
    return (nextpos[0], nextpos[1])

  def step(self, mymap):
    nextpos = self.getNextValidStep(mymap)
    # print("moving to ", nextpos)
    if mymap[nextpos[0]][nextpos[1]] != 'X':
      self.stepsTaken += 1
    mymap[nextpos[0]][nextpos[1]] = directions[self.face]
    mymap[self.row][self.col] = 'X'
    self.row = nextpos[0]
    self.col = nextpos[1]
  
class GuardLoopError(Exception):
  pass

class GuardStuckError(Exception):
  pass

themap = []
with open("input.txt") as f:
  for row, line in enumerate(f):
    maprow = []
    for col, char in enumerate(line.strip()):
      if char in directions:
        guard = Guard(row, col, directions.index(char))
      maprow.append(char)
    themap.append(maprow)

firstrun = True
loops = 0
while 0 < guard.row < len(themap[0]) - 1 and 0 < guard.col < len(themap) - 1:
  if not firstrun:
    testmap = [row[:] for row in themap]
    testguard = Guard(guard.row, guard.col, guard.face)
    nextspot = testguard.getNextStepPos(testmap)
    if testmap[nextspot[0]][nextspot[1]] not in ["#", "X"]:
      testmap[nextspot[0]][nextspot[1]] = "#"

      try:
        while 0 < testguard.row < len(testmap[0]) - 1 and 0 < testguard.col < len(testmap) - 1:
          testguard.step(testmap)
      except GuardLoopError:
        loops += 1
      except GuardStuckError:
        continue
      
  else:
    firstrun = False
  guard.step(themap)
  # print("guard is at %s,%s, facing %s" % (guard.row, guard.col, directions[guard.face]))

# for row in themap:
#   print(''.join(row))

print(loops)
