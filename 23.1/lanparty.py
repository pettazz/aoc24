connections = []

with open("input.txt") as f:
  for line in f:
    if line.strip() != "":
      connections.append(sorted(line.strip().split("-")))

adjs = {}
while connections:
  duo = connections.pop()
  for i in (0, 1):
    compy = duo[i]
    if compy not in adjs.keys():
      adjs[compy] = set()
    adjs[compy].add(duo[i ^ 1])

throuples = set()
for node, buddies in adjs.items():
  for buddy in buddies:
    for maybeBuddy in adjs[buddy]:
      if not maybeBuddy == node and node in adjs[maybeBuddy]:
        throuple = (*sorted((node, buddy, maybeBuddy)),)
        if node.startswith('t') or buddy.startswith('t') or maybeBuddy.startswith('t'):
          throuples.add(throuple)
print(len(throuples))