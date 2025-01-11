connections = []

with open("input.txt") as f:
  for line in f:
    if line.strip() != "":
      connections.append(line.strip().split("-"))

adjs = {}
while connections:
  duo = connections.pop()
  for i in (0, 1):
    compy = duo[i]
    if compy not in adjs.keys():
      adjs[compy] = set()
    adjs[compy].add(duo[i ^ 1])

polycules = {}
for node, buddies in adjs.items():
  neighborhood = sorted([node] + list(buddies))
  for buddy in buddies:
    polycule = (*[n for n in neighborhood if n in adjs[buddy]], buddy)
    if polycule not in polycules.keys():
      polycules[polycule] = set()
    polycules[polycule].add(node)

largest = (0, 0)
for polycule, nodes in polycules.items():
  # print(polycule, len(nodes))
  if len(nodes) > largest[1]:
    largest = (polycule, len(nodes))

print("largest:", largest)
print("password:", ",".join(sorted(largest[0])))