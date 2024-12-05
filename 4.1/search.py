count = 0
mul = range(-1,2)
con = range(1,4)

with open("input.txt") as f:
  rows = [line for line in f]

for idx, row in enumerate(rows):
  stridx = 0
  while stridx < len(row):
    xpos = row.find('X', stridx)
    if xpos == -1:
      break 
    
    for m in mul:
      for n in mul:
        foundstr = 'X'
        for c in con:
          x = idx+c*m
          y = xpos+c*n

          if (-1 < x < len(rows)) and (-1 < y < len(row)):
            foundstr += rows[x][y]
        if foundstr == "XMAS":
          count +=1
    
    stridx = xpos + 1

print(count)