import math

robots = []

with open("input.txt") as f:
  for line in f:
    if line.strip():
      parts = line.split(" ")
      startpos = (*[i for i in map(int, parts[0].strip().split("=")[1].split(","))],)
      velo = (*[i for i in map(int, parts[1].strip().split("=")[1].split(","))],)
      robots.append([startpos, velo])

bounds = (101, 103)
midx = bounds[0] // 2
midy = bounds[1] // 2

def isunique(time):
  positions = []

  for bot in robots:
    pos = bot[0]
    vel = bot[1]
    loopsx, futurex = divmod(pos[0] + (vel[0] * time), bounds[0])
    loopsy, futurey = divmod(pos[1] + (vel[1] * time), bounds[1])
    if (futurex, futurey) in positions:
      return False
    positions.append((futurex, futurey))

  rows = []
  for y in range(bounds[1]):
    row = ""
    for x in range(bounds[0]):  
      if (x,y) in positions:
        row += "1"
      else:
        row += "."
    rows.append(row)

  for r in rows:
    print(r)
  return True


for t in range(10000):
  if isunique(t):
    print(t)
    break