wires = {}
gates = []
zs = []

with open("input.txt") as f:
  for line in f:
    if line.strip() == "":
      break
    parts = line.strip().split(": ")
    wires[parts[0]] = parts[1]
  for line in f:
    if line.strip() == "":
      break
    parts = line.strip().split(" ")
    # 0: input1, 1: input2, 2: gate op, 3: output
    gates.append((parts[0], parts[2], parts[1], parts[4]))
    if parts[4].startswith("z"):
      zs.append(parts[4])
      zs.sort()

def gateop(wire1, wire2, op):
  i1, i2 = wires[wire1], wires[wire2]
  if op == "AND":
    return str(int(i1 == i2 and i1 == "1"))
  if op == "OR":
    return str(int(i1 == "1" or i2 == "1"))
  if op == "XOR":
    return str(int(i1 != i2))
  return None

while zs:
  for gate in gates:
    if gate[0] in wires.keys() and gate[1] in wires.keys():
      if gate[3] not in wires.keys():
        wires[gate[3]] = gateop(gate[0], gate[1], gate[2])
        # print(wires[gate[0]], gate[2], wires[gate[1]], "->", gate[3], wires[gate[3]])

  if all([z in wires for z in zs]):
    break

bin = "".join([wires[z] for z in zs[::-1]])
print(int(bin, 2))