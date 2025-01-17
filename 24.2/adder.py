import random

def bitter(wire, bit):
  return "" + wire + str(bit).zfill(2)

def getGate(input1, input2, gate):
  if (input1, input2, gate) in gates.keys():
    return (input1, input2, gate)
  elif (input2, input1, gate) in gates.keys():
    return (input2, input1, gate)
  else:
    return None

def getOutputWire(input1, input2, gate):
  gate = getGate(input1, input2, gate)
  if gate:
    return gates[gate]
  else:
    return None

def gateop(wiredefs, wire1, wire2, op):
  i1, i2 = wiredefs[wire1], wiredefs[wire2]
  if op == "AND":
    return str(int(i1 == i2 and i1 == "1"))
  if op == "OR":
    return str(int(i1 == "1" or i2 == "1"))
  if op == "XOR":
    return str(int(i1 != i2))
  return None

def runAdder(awires, agates, azs):
  mywires = awires.copy()
  prevstate = 0
  while azs:
    for gate, output in agates.items():
      if gate[0] in mywires.keys() and gate[1] in mywires.keys():
        if output not in mywires.keys():
          mywires[output] = gateop(mywires, gate[0], gate[1], gate[2])

    if all([z in mywires for z in azs]):
      break
    else:
      if len(mywires) == prevstate:
        raise RuntimeException("loop!")
      else:
        prevstate = len(mywires)

  return "".join([mywires[z] for z in azs[::-1]])

wires = {}
gates = {}
zcounter = 0

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
    # (0: input1, 1: input2, 2: gate op) => output
    gates[(parts[0], parts[2], parts[1])] = parts[4]
    if parts[4].startswith("z"):
      zcounter += 1

zs = [bitter("z", z) for z in range(zcounter)]

xinput = "".join([wires[bitter("x", x)] for x in reversed(range(zcounter - 1))])
yinput = "".join([wires[bitter("y", y)] for y in reversed(range(zcounter - 1))])
ztarget = str(bin(int(xinput, 2) + int(yinput, 2)))[2:]

swappers = []
carryw = None
bit = 0
while bit < len(zs) - 1:
  # print(bit)
  xwire = bitter("x", bit)
  ywire = bitter("y", bit)
  zwire = bitter("z", bit)

  # follow carry adder structure to find incorrect wiring
  if bit == 0:
    carryw = getOutputWire(xwire, ywire, "AND")
  else:
    xorout = getOutputWire(xwire, ywire, "XOR")
    andout = getOutputWire(xwire, ywire, "AND")
    # print(xorout, carryw)
    carryxorout = getOutputWire(xorout, carryw, "XOR")

    if carryxorout is None:
      # print("no carryx", [xorout, andout])
      swappers += [xorout, andout]
      gates[getGate(xwire, ywire, "XOR")] = andout
      gates[getGate(xwire, ywire, "AND")] = xorout
      bit = 0
      continue

    if carryxorout != zwire:
      # print("carryx isnt z", [zwire, carryxorout])
      swappers += [zwire, carryxorout]
      zkey = next(filter(lambda g: g[1] == zwire, gates.items()))[0]
      gates[zkey] = carryxorout
      gates[getGate(xorout, carryw, "XOR")] = zwire
      bit = 0
      continue

    carryandout = getOutputWire(xorout, carryw, "AND")
    carryw = getOutputWire(andout, carryandout, "OR")

  bit += 1

print("correct sum:", ztarget)
print("is it fixed:", runAdder(wires.copy(), gates, zs))

print(",".join(sorted(swappers)))