count = 0

with open("input.txt") as f:
  rows = [line for line in f]

for idx, row in enumerate(rows):
  stridx = 0
  while stridx < len(row):
    xpos = row.find('A', stridx)
    if xpos == -1:
      break 
    
    foundchars = []
    for mulx in (-1, 1):
      for muly in (-1, 1):
        x = idx + mulx
        y = xpos + muly
        if (-1 < x < len(rows)) and (-1 < y < len(row)):
          val = rows[x][y]
        else:
          val = '.'
        foundchars.append(val)
        
    if ((foundchars[0] == 'M' and foundchars[3] == 'S') or (foundchars[0] == 'S' and foundchars[3] == 'M'))\
       and ((foundchars[1] == 'M' and foundchars[2] == 'S') or (foundchars[1] == 'S' and foundchars[2] == 'M')):
       count += 1
    
    stridx = xpos + 1

print(count)