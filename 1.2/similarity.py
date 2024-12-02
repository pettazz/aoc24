l,r  = [], []

with open('input.txt') as f:
  for line in f:
    l.append(int(line.split()[0]))
    r.append(int(line.split()[1]))

l.sort()
r.sort()

score = 0
ridx = 0

for num in l:
  rcount = 0

  while r[ridx] < num:
    ridx += 1

  while r[ridx] == num:
    rcount += 1
    ridx += 1

  score += num * rcount

print(score)