# numeric pad
# ---
# grug brained approach here because its small enough
# that this is probably faster than a bfs or whatever
# lets see if i live to regret this in part 2
def toNumRow(key):
  if key in [1, 2, 3]:
    return 1
  elif key in [4, 5, 6]:
    return 2
  elif key in [7, 8, 9]:
    return 3
  else:
    return 0

def toNumCol(key):
  if key in [7, 4, 1]:
    return 0
  elif key in [8, 5, 2, 0]:
    return 1
  else:
    return 2

def makeNumMove(current, direction):
  if direction == "A":
    return current
  if direction == ">":
    if current == 0:
      return 0.5
    else:
      return current + 1
  if direction == "<":
    if current == 0.5:
      return 0
    else:
      return current - 1
  if direction == "^":
    if current == 0:
      return 2
    elif current == 0.5:
      return 3
    else:
      return current + 3
  if direction == "v":
    if current == 2:
      return 0
    elif current == 3:
      return 0.5
    else:
      return current - 3

def getNumDirection(position, wanted):
  # print("position, wanted", position, wanted)
  diff = wanted - position
  if wanted in [0, 0.5]:
    if position in [7, 4, 1]:
      return ">"
  # print("diff", diff)
  if diff == 0:
    return "A"

  if diff > 0:
    # vertical first
    currRow = toNumRow(position)
    wantRow = toNumRow(wanted)
    if currRow < wantRow:
      return "^"
    elif currRow > wantRow:
      return "v"
    else:
      return ">"
  else: 
    # horizontal first
    currCol = toNumCol(position)
    wantCol = toNumCol(wanted)
    if currCol > wantCol:
      return "<"
    elif currCol > wantCol:
      return ">"
    else:
      return "v"

# directional pad
# ---

def toPos(key):
  match key:
    case "A":
      return (2, 0)
    case "^":
      return (1, 0)
    case "<":
      return (0, 1)
    case "v":
      return (1, 1)
    case ">":
      return (2, 1)

def fromPos(key):
  match key:
    case (2, 0):
      return "A"
    case (1, 0):
      return "^"
    case (0, 1):
      return "<"
    case (1, 1):
      return "v"
    case (2, 1):
      return ">"

def getArrowStep(current, wanted):
  if current == wanted:
    return "A", current

  # just manually handle the blank spot
  if current == "^" and wanted == "<":
    return "v", "v"
  if current == "<":
    return ">", "v"

  currPos = toPos(current)
  wantPos = toPos(wanted)

  newx, newy = currPos[0], currPos[1]
  dx = currPos[0] - wantPos[0]
  # print("dx", dx)
  if dx != 0:
    if dx < 0:
      newx = currPos[0] + 1
      direction = ">" 
    else:
      newx = currPos[0] - 1
      direction = "<"
  else:
    dy = currPos[1] - wantPos[1]
    # print("dy", dy)
    if dy != 0:
      if dy < 0:
        newy = currPos[1] + 1
        direction = "v"
      else:
        newy = currPos[1] - 1
        direction = "^"

  return direction, fromPos((newx, newy))

mtsCache = {}
def moveToSequence(move, startPos):
  if (move, startPos) in mtsCache.keys():
    return mtsCache[(move, startPos)]
  moves = []
  pos = startPos
  step = None
  while step != "A":
    # print("curr, want", pos, move)
    step, pos = getArrowStep(pos, move)
    # print("step, to", step, pos)
    moves.append(step)
  # print("---")
  mtsCache[(move, startPos)] = (moves, pos)
  return moves, pos

mlCache = {}
def movesLength(move, startPos, depth=0):
  if (move, startPos, depth) in mlCache.keys():
    return mlCache[(move, startPos, depth)]
  length = 0
  if depth == 0:
    return 1
  newMoves, startPos = moveToSequence(move, startPos)
  for move in newMoves:
    length += movesLength(move, startPos, depth-1)
  mlCache[(move, startPos, depth)] = length
  return length

codes = []
with open("input.txt") as f:
  for line in f:
    code = []
    if line.strip() != "":
      for char in line.strip():
        if char == "A":
          code.append(0.5)
        else:
          code.append(int(char))
    codes.append(code)

complexityCounter = 0
for code in codes:
  numPosition = 0.5
  length = 0
  for char in code:
    move = None
    while move != "A":
      move = getNumDirection(numPosition, char)
      
      length += movesLength(move, "A", 56)

      goto = makeNumMove(numPosition, move)
      numPosition = goto

  def stringit(char):
    return str(char) if char != 0.5 else "A"

  print("%s: " % "".join([stringit(c) for c in code]))

  num = int("".join([str(i) for i in code[:-1]]))
  print(length, num)
  complexityCounter += length * num

print("total", complexityCounter)