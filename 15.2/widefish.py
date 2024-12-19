def dirchange(char):
  directions = ["^", ">", "v", "<"]
  dirchanges = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  return dirchanges[directions.index(char)]

def tupadd(one, two):
  return (one[0] + two[0], one[1] + two[1])

def mappos(pos):
  return themap[pos[0]][pos[1]]

themap = []
moves = []
fishpos = (0,0)

with open("input.txt") as f:
  # map first
  for y, line in enumerate(f):
    if line.strip():
      row = []
      for x, char in enumerate(line.strip()):
        if char == "@":
          fishpos = (y, 2*x)
          widerchar = ["@", "."]
        elif char == ".":
          widerchar = [".", "."]
        elif char == "#":
          widerchar = ["#", "#"]
        else:
          widerchar = ["[", "]"]
        row += widerchar
      themap.append(row)
    else:
      break

  #then moves
  for line in f:
    if line.strip():
      for char in line.strip():
        moves.append(char)

def printmap():
  for row in themap:
    rowstr = ""
    for col in row:
      rowstr += col
    print(rowstr)

def canmove(pos, direction):
  testpos = tupadd(pos, direction)
  if mappos(testpos) == "#":
    # print("against a wall somewhere")
    return False
  if mappos(testpos) == "[":
    return canmove(testpos, direction) and canmove(tupadd(testpos, dirchange(">")), direction)
  elif mappos(testpos) == "]":
    return canmove(testpos, direction) and canmove(tupadd(testpos, dirchange("<")), direction)
  else:
    return True

def domove(pos, direction):
  global fishpos
  newpos = tupadd(pos, direction)
  # print(pos, direction, newpos, mappos(newpos))
  if mappos(newpos) == "[":
    # print("move right", tupadd(newpos, dirchange(">")))
    domove(newpos, direction)
    domove(tupadd(newpos, dirchange(">")), direction)
  elif mappos(newpos) == "]":
    # print("move left", tupadd(newpos, dirchange("<")))
    domove(newpos, direction)
    domove(tupadd(newpos, dirchange("<")), direction)

  if mappos(pos) == "@":
    fishpos = newpos

  # print("swap", pos, newpos)
  themap[pos[0]][pos[1]], themap[newpos[0]][newpos[1]] = \
    themap[newpos[0]][newpos[1]], themap[pos[0]][pos[1]]

printmap()
for move in moves:
  print("moving", move)
  direction = dirchange(move)
  if move in ["<", ">"]:
    moveables = [fishpos]
    testpos = tupadd(fishpos, direction)
    while mappos(testpos) not in [".", "#"]:
      moveables.append(testpos)
      testpos = tupadd(testpos, direction)
    if mappos(testpos) == "#":
      # print("against the wall")
      continue
    else:
      for oldpos in moveables[::-1]:
        newpos = tupadd(oldpos, direction)
        char = mappos(oldpos)
        themap[newpos[0]][newpos[1]] = char
        if char == "@":
          themap[oldpos[0]][oldpos[1]] = "."
          fishpos = newpos
        else:
          themap[oldpos[0]][oldpos[1]] = char
  else:
    if canmove(fishpos, direction):
      domove(fishpos, direction)
printmap()

total = 0
for y, row in enumerate(themap):
  for x, col in enumerate(row):
    if col == "[":
      total += 100*y + x
print("gps", total)