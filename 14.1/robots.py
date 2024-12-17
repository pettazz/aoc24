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

positions = []

for bot in robots:
  pos = bot[0]
  vel = bot[1]
  loopsx, futurex = divmod(pos[0] + (vel[0] * 100), bounds[0])
  loopsy, futurey = divmod(pos[1] + (vel[1] * 100), bounds[1])
  positions.append((futurex, futurey))

# for y in range(bounds[1]):
#   row = ""
#   for x in range(bounds[0]):
#     if y == midy or x == midx:
#       row += " "
#     else:
#       poscount = len([pos for pos in positions if pos == (x,y)])
#       if poscount:
#         row += "%s" % poscount
#       else:
#         row += "."
#   print(row)

quads = [0]*4
quads[0] = len([p for p in positions if p[0] < midx and p[1] < midy])
quads[1] = len([p for p in positions if p[0] > midx and p[1] < midy])
quads[2] = len([p for p in positions if p[0] < midx and p[1] > midy])
quads[3] = len([p for p in positions if p[0] > midx and p[1] > midy])
# print(quads)
print(math.prod(quads))