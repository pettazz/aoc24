total = 0
l,r  = [], []
with open('input.txt') as f:
  for line in f:
    l.append(int(line.split()[0]))
    r.append(int(line.split()[1]))

l.sort()
r.sort()

for i in range(len(l)):
  total += abs(l[i] - r[i])

print(total)