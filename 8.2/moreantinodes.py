count = 0
freqs = {}

maxrow = 0
with open("input.txt") as f:
  for rowidx, line in enumerate(f):
    line = line.strip()
    if line == "":
      break
    maxrow += 1
    maxcol = len(line) - 1
    for colidx, char in enumerate(line):
      if char != ".":
        if char in freqs.keys():
          freqs[char].append((rowidx, colidx))
        else:
          freqs[char] = [(rowidx, colidx)]
bounds = (maxrow - 1, maxcol)

def find_antinodes(nodelist, bounds):
  antinodes = []
  if len(nodelist) > 1:
    node = nodelist[:1][0]
    # each iter, draw a line between first node and each of the remaining, reduce 
    for othernode in nodelist[1:]:
      dy = node[0] - othernode[0]
      dx = node[1] - othernode[1]

      yline = node[0]
      xline = node[1]
      while 0 <= yline <= bounds[0] and 0 <= xline <= bounds[1]:
        antinodes.append((yline, xline))
        yline += dy
        xline += dx

      yline = node[0]
      xline = node[1]
      while 0 <= yline <= bounds[0] and 0 <= xline <= bounds[1]:
        antinodes.append((yline, xline))
        yline = yline - dy
        xline = xline - dx

      # print('----')
      # print(node, othernode, candidates)
      # print('----')
      # for r in range(bounds[0] + 1):
      #   row = ""
      #   for c in range(bounds[1] + 1):
      #     if (r, c) == node or (r, c) == othernode:
      #       row += "n"
      #     elif (r, c) in candidates:
      #       row += "#"
      #     else:
      #       row += "."
      #   print(row)
    return antinodes + find_antinodes(nodelist[1:], bounds)
  else:
    return antinodes

antinodes = set()
for freq, nodes in freqs.items():
  if len(nodes) < 2:
    continue

  antinodes.update(find_antinodes(nodes, bounds))

print(len(antinodes))

# 913 too low