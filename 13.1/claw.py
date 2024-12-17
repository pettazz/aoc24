def lcmopps(a, b):
  def gcd(n, m):
    return gcd(m, n % m) if m > 0 else n
  lcm = int(a * b / gcd(a, b))
  return (int(lcm / a), int(lcm / b))

machines = []
with open("input.txt") as f:
  machine = {}
  for line in f:
    if line.startswith("Button"):
      parts = line.strip().split("+")
      x = int(parts[1].split(",")[0])
      y = int(parts[2])

      if line.startswith("Button A"):
        machine["a"] = (x, y)
      else:
        machine["b"] = (x, y)
    elif line.startswith("Prize"):
      parts = line.strip().split("=")
      x = int(parts[1].split(",")[0])
      y = int(parts[2])
      machine["prize"] = (x, y)
      machines.append(machine)
      machine = {}

total = 0
for mach in machines:
  acoef, bcoef = lcmopps(*mach["a"])
  bside = bcoef * mach["b"][1] - acoef * mach["b"][0]
  pside = bcoef * mach["prize"][1] - acoef * mach["prize"][0]
  bval, brem = divmod(pside, bside)
  if brem > 0:
    # print("this machine is a liar")
    continue

  aval, arem = divmod(mach["prize"][0] - (mach["b"][0] * bval), mach["a"][0])
  if arem > 0:
    # print("this machine is a sneaky liar")
    continue

  # print("a, b:", aval, bval)
  if aval <= 100 and bval <= 100:
    total += aval * 3 + bval

print(total)