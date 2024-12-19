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
          fishpos = (y, x)
        row.append(char)
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

printmap()
for move in moves:
  print("moving", move)
  direction = dirchange(move)
  moveables = [fishpos]
  testpos = tupadd(fishpos, direction)
  while mappos(testpos) not in [".", "#"]:
    moveables.append(testpos)
    testpos = tupadd(testpos, direction)
  if mappos(testpos) == "#":
    print("against the wall")
    continue
  else:
    print(moveables)
    for oldpos in moveables[::-1]:
      newpos = tupadd(oldpos, direction)
      char = mappos(oldpos)
      print("replacing", oldpos, newpos, char)
      themap[newpos[0]][newpos[1]] = char
      if char == "@":
        themap[oldpos[0]][oldpos[1]] = "."
        fishpos = newpos
      else:
        themap[oldpos[0]][oldpos[1]] = char
  printmap()

total = 0
for y, row in enumerate(themap):
  for x, col in enumerate(row):
    if col == "O":
      total += 100*y + x
print("gps", total)